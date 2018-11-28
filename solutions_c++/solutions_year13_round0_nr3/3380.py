#include <iostream>
#include "BigInteger.h"
#include <vector>
using namespace std;

BigInteger::BigInteger() {
}

BigInteger::BigInteger(int n) {
    container = to_string(n);
}

BigInteger::BigInteger(string& str) {
    container = str;
}

BigInteger BigInteger::operator+(BigInteger& other) {    
    string str1 = container;
    string str2 = other.container;
    if (str1.size() < str2.size()) swap(str1, str2);
    int diff = str1.size() - str2.size();
    for (int i = 0; i < diff; i++)
        str2 = string("0") + str2;
    long carry = 0;
    vector<long> vec;
    string str = "";
    for (long i = str1.length() - 1, j = str2.length() - 1; i >= 0 ; i--, j--) {
        long x = 0;
        x = carry + from_string<long>(str1.substr(i,1)) + from_string<long>(str2.substr(j,1));
        carry = x / 10;
        str = to_string(x%10) + str;
    }
    if (carry != 0) str = to_string(carry) + str;
    return BigInteger(str);
}

BigInteger BigInteger::operator+(int number) {
    string str2 = to_string(number);
    string str1 = container;
    long carry = 0;
    vector<long> vec;
    string str = "";
    for (long i = str1.length() - 1, j = str2.length() - 1; i >= 0 ; i--, j--) {
        long x = 0;
        if (j >= 0)
            x = carry + from_string<long>(str1.substr(i,1)) + from_string<long>(str2.substr(j,1));
        else
            x = carry + from_string<long>(str1.substr(i,1));
        carry = x / 10;
        str = to_string(x%10) + str;
    }
    if (carry == 1) str = to_string(1) + str;
    return BigInteger(str);
}

BigInteger BigInteger::operator*(BigInteger& other) {    
    string str2 = other.container;
    string appendString = "";    
    string first = string("0");
    BigInteger result = BigInteger(first);
    for (int j = str2.size() - 1; j >= 0; j--) {
        BigInteger temp = (*this) * from_string<long>(str2.substr(j,1));
        temp = temp.append(appendString);
        appendString = "0" + appendString;
        result = result + temp;
    }
    return result;
}

BigInteger BigInteger::operator*(int number) {
    string str = container;
    long carry = 0;
    string result = "";
    for (long i = str.size() - 1; i >=0; i--) {
        long x = 0;
        x = carry + from_string<long>(str.substr(i,1)) * number;
        carry = x/10;
        result = to_string(x%10) + result;
    }
    if (carry != 0) result = to_string(carry) + result;
    return BigInteger(result);
}

bool BigInteger::operator<=(const BigInteger& bigInteger) {
    if (container.length() > bigInteger.container.length())
        return false;
    if (container.length() < bigInteger.container.length())
        return true;
    for (int i = 0; i < container.length(); i++) {
        if (container[i] == bigInteger.container[i])
            continue;
        if (container[i] < bigInteger.container[i])
            return true;
        if (container[i] > bigInteger.container[i])
            return false;
    }
    return true;
}

bool BigInteger::operator<(const BigInteger bigInteger) {
    if (container.length() > bigInteger.container.length())
        return false;
    if (container.length() < bigInteger.container.length())
        return true;
    for (int i = 0; i < container.length(); i++) {
        if (container[i] == bigInteger.container[i])
            continue;
        if (container[i] < bigInteger.container[i])
            return true;
        if (container[i] > bigInteger.container[i])
            return false;
    }
    return false;
}

bool BigInteger::operator>=(const BigInteger& bigInteger) {
    if (container.length() > bigInteger.container.length())
        return true;
    if (container.length() < bigInteger.container.length())
        return false;
    for (int i = 0; i < container.length(); i++) {
        if (container[i] == bigInteger.container[i])
            continue;
        if (container[i] < bigInteger.container[i])
            return false;
        if (container[i] > bigInteger.container[i])
            return true;
    }
    return true;
}

bool BigInteger::operator==(const BigInteger& bigInteger) {
    if (container.compare(bigInteger.container) == 0)
        return true;
    else
        return false;
        
}

BigInteger& BigInteger::operator=(const BigInteger& bigInteger) {
    container = bigInteger.container;
    return *this;
}

long BigInteger::IntegerValue() {
    return from_string<long>(container);
}

BigInteger BigInteger::append(string str) {
    string contains = container;
    string result = contains + str;
    return BigInteger(result);
}

bool BigInteger::isPalindrom() {
    for (int i = container.size()-1, j = 0; i >= 0 && j < container.size(); i--, j++)
        if (container[i] != container[j])   return false;
    return true;
}

std::ostream& operator<< (std::ostream &out, BigInteger& bInteger)
{
    out << bInteger.container << " ";
    return out;
}

