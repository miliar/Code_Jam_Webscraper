/*
ID: zachary11
PROG: calfflac
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <stdio.h>

using namespace std;

template <typename Type>
string toString(Type t){
	stringstream ss;
        string s;
	ss << t;
        ss >> s;
        return s;
}

template <typename Type>
char toChar(Type t){
	stringstream ss;
        char s;
	ss << t;
        ss >> s;
        return s;
}

template <typename Type>
int toInt(Type t){
	stringstream ss;
        int i;
	ss << t;
        ss >> i;
        return i;
}

string reverse(string s){
    string result = "";
    for(int i=0; i<s.length(); i++) result = s[i] + result;
    return result;
}

bool isPalindromic(string s){
    return ((s.length() == 0 || s.length() == 1)
            ||(s[0]==s[s.length()-1] && isPalindromic(s.substr(1,s.length()-2))));
}

bool isPalindromic(int s){
    return isPalindromic(toString(s));
}

void nextPalindromeBrute(int &i){
    i++;
    while(!isPalindromic(toString(i))) i++;
}

void nextPalindrome(int &i){
    string s = toString(i);
    int halfLength = floor(s.length()/2);
    if(s.length()%2 == 0){
        string half = s.substr(0,halfLength);
        int added = toInt(half) + 1;
        half = toString(added);
        if(half.length() == halfLength){
            i = toInt(half + reverse(half));
        } else {
            i = toInt(half + reverse(half).substr(1));
        }
    } else {
        int mid = toInt(s[halfLength]);
        if(mid!=9){
            s[halfLength] = toChar(++mid);
            i = toInt(s);
        } else {
            string half = s.substr(0,halfLength);
            int added = toInt(half) + 1;
            half = toString(added);
            if(half.length() == halfLength){
                i = toInt(half + '0' + reverse(half));
            } else {
                i = toInt(half + reverse(half));
            }
        }
    }
}

int countFairSquares(int current, int max){
    int count = 0;
    if(isPalindromic(current) && isPalindromic(current*current)) count++;
    nextPalindromeBrute(current);
    while(current<=max){
        if(isPalindromic(current*current)) count++;
        nextPalindrome(current);
    }
    return count;
}

int main() {
    ofstream fout("codeJam.out");
    ifstream fin("codeJam.in");
    int caseNumber=0;
    fin >> caseNumber;
    for(int i=1; i<=caseNumber; i++){
        int min=0,max=0;
        fin >> min >> max;
        fout << "Case #" << i << ": " << countFairSquares(ceil(sqrt(min)), floor(sqrt(max))) << endl;
    }
    
    return 0;
}
