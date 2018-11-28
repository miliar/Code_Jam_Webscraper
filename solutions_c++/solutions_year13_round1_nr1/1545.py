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

long countRings(long long radius, long long paint){
    long count = 0;
    while(true){
        long long paintNeeded = 2*radius+1;
        if(paint >= paintNeeded){
            count++;
            radius+=2;
            paint-=paintNeeded;
        } else {
            return count;
        }
    }
}

int main() {
    ofstream fout("codeJam.out");
    ifstream fin("codeJam.in");
    long caseNumber=0;
    fin >> caseNumber;
    for(long i=1; i<=caseNumber; i++){
        
        long long startR, paint;
        fin >> startR >> paint;
        
        string solution = toString(countRings(startR, paint));
        fout << "Case #" << i << ": " << solution << endl;
        cout << "Case #" << i << ": " << solution << endl;
    }
    
    return 0;
}
