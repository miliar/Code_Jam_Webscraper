//
//  A Small.cpp
//  Code Jam
//
//  Created by Thanadee Wangrotjanarat on 4/11/2558 BE.
//  Copyright (c) 2558 professional computer. All rights reserved.
//



#include <cstdint>
#include <cstring>

namespace TND{
    class CharSequence {
    public:
        virtual operator char const*() const = 0;
        bool operator == (CharSequence const& other) const;
        bool operator != (CharSequence const& other) const{
            return !operator==(other);
        }
        bool operator == (char const* other) const;
        bool operator != (char const* other) const{
            return !operator==(other);
        }
    };
    class String: public CharSequence {
        class Private;
        Private* pv;
    public:
        static const String endl;
        
        String();
        String(const String &copy);
        String(String&& move);
        explicit String(int value);
        explicit String(long long value);
        explicit String(double value);
        String(const char* fromUTF8);
        String(const char* fromUTF8, size_t length);
        String& operator=(const String& copy);
        String& operator=(String&& move);
        ~String();
        
        operator const char*() const override;
        explicit operator int() const;
        explicit operator double() const;
        
        void operator += (const String &other);
        void operator += (const char *str);
        
        size_t length() const;
        bool operator < (const String &other) const;
        bool operator == (const String &other) const;
        bool operator != (const String &other) const{
            return !operator==(other);
        }
        using CharSequence::operator==;
        String operator+(const char *str) const;
        String operator+(const String& other) const;
        String subString(size_t index, size_t last) const;
    };
}

//
//  String.cpp
//  OpenGL Game
//
//  Created by Thanadee Wangrotjanarat on 2/11/2558 BE.
//  Copyright (c) 2558 Thanadee Wangrotjanarat. All rights reserved.
//
#include <cstring>
#include <string>
#include <locale>

using namespace std;
using namespace TND;

bool CharSequence::operator == (TND::CharSequence const &other) const{
    return strcmp(this->operator char const *(), other.operator char const *()) == 0;
}

bool CharSequence::operator == (char const *other) const{
    return strcmp(this->operator char const *(), other) == 0;
}

class String::Private {
    Private(Private&) = delete;
    Private& operator=(const Private&) = delete;
    size_t ensureSize(size_t newSize){
        auto oldSize = size;
        if (newSize > length + 1) {
            length = newSize + 1;
            auto newStr = new char[length];
            memcpy(newStr, str, size * sizeof(char));
            delete[] str;
            str = newStr;
        }
        size = newSize;
        return oldSize;
    }
public:
    char *str;
    size_t size;
    size_t length;
    Private(size_t initialSize) : str(new char[initialSize + 1]), size(0), length(initialSize + 1){}
    ~Private(){
        delete[] str;
    }
    void appendStr(char const * copy, size_t copySize){
        auto oldSize = ensureSize(size + copySize);
        memcpy(str + oldSize, copy, copySize * sizeof(char));
    }
};

const String String::endl = "\r\n";

String::String() : pv(new Private(255)){}
String::String(const String& copy) : pv(new Private(copy.pv->size)){
    pv->appendStr(copy.pv->str, copy.pv->size);
}
String::String(String&& move) : pv(move.pv){
    move.pv = 0;
}
String::String(int value) : pv(new Private(10))
{
    auto str = std::to_string(value);
    pv->appendStr(str.c_str(), str.size());
}
String::String(long long value) : pv(new Private(10))
{
    auto str = std::to_string(value);
    pv->appendStr(str.c_str(), str.size());
}

String::String(double value): pv(new Private(30)){
    auto str = std::to_string(value);
    pv->appendStr(str.c_str(), str.size());
}

String::String(const char* str) : pv(new Private(255)) {
    pv->appendStr(str, strlen(str));
}

String::String(const char* str, size_t length): pv(new Private(length)){
    pv->appendStr(str, length);
}

String& String::operator=(const String& copy){
    delete pv;
    pv = new Private(copy.pv->size);
    pv->appendStr(copy.pv->str, copy.pv->size);
    return *this;
}

String& String::operator=(String&& move){
    delete pv;
    pv = move.pv;
    move.pv = 0;
    return *this;
}

String::~String()
{
    delete pv;
}

String::operator const char*() const{
    pv->str[pv->size] = '\0';
    return pv->str;
}
String::operator int() const{
    pv->str[pv->size] = '\0';
    return static_cast<int>(strtol(pv->str, 0, 0));
}
String::operator double() const{
    pv->str[pv->size] = '\0';
    return strtod(pv->str, 0);
}

void String::operator+=(const String &other){
    pv->appendStr(other.pv->str, other.pv->size);
}

void String::operator += (const char *str){
    pv->appendStr(str, strlen(str));
}

size_t String::length() const{
    return pv->size;
}

bool String::operator < (const String &other) const{
    if (pv->size == other.pv->size) {
        return memcmp(pv->str, other.pv->str, pv->size * sizeof(char)) < 0;
    }
    else {
        return pv->size < other.pv->size;
    }
}

bool String::operator == (const String &other) const{
    if (pv->size == other.pv->size) {
        return memcmp(pv->str, other.pv->str, pv->size * sizeof(char)) == 0;
    }
    else {
        return false;
    }
}

String String::subString(size_t index, size_t last) const{
    String newStr(pv->str + index, last - index);
    return newStr;
}

String String::operator+(const char *str) const
{
    String newStr{ *this };
    newStr += str;
    return newStr;
}
String String::operator+(const String& other) const
{
    String newStr{ *this };
    newStr += other;
    return newStr;
}


#include <iostream>
#include <cmath>
//#define DEBUGING
#ifdef DEBUGING
#define printVar(varName) std::cout << #varName ": " << varName << std::endl;
#else
#define printVar(varName)
#endif
using namespace std;
using namespace TND;

size_t calMoveTurn(size_t* pancakes, size_t size, size_t divider){
    size_t sum = 0;
    for (size_t i = 0; i < size; ++i) {
        sum += (pancakes[i] - 1) / divider;
    }
    return sum + divider;
}

void InfiniteHouseofPancakes(size_t testCaseNum){
    size_t numPancakes, maxPancakes = 0;
    cin >> numPancakes;
    auto pancakes = new size_t[numPancakes];
    for (size_t i = 0; i < numPancakes; ++i) {
        cin >> pancakes[i];
        printVar(pancakes[i]);
        maxPancakes = maxPancakes > pancakes[i] ? maxPancakes : pancakes[i];
    }
    size_t turnNeeded = ~size_t{0};
    for (size_t i = 1; i <= maxPancakes; ++i) {
        auto caled = calMoveTurn(pancakes, numPancakes, i);
        turnNeeded = turnNeeded < caled ? turnNeeded : caled;
    }
    cout << "Case #" << testCaseNum << ": " << turnNeeded << endl;
    delete[] pancakes;
}

void testCase(void(*aFunction)(size_t)){
    size_t testCase;
    cin >> testCase;
    printVar(testCase);
    for (size_t i = 0; i < testCase; ++i) {
        aFunction(i + 1);
    }
}

int main(){
    testCase(&InfiniteHouseofPancakes);
}