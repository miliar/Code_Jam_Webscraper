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
#include <set>

using namespace std;

template <typename Type>
string toString(Type t){
	stringstream ss;
        string s;
	ss << t;
        ss >> s;
        return s;
}

bool isConsonant(char c){
    if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u') return false;
    else return true;
}

void addPermutations(int start, set<string> &permutations, int length,int n){
    int end = start+n-1;
    for(int i=start; i>=0; i--){
        for(int j=end; j<length; j++){
            permutations.insert( toString(i) + "-" + toString(j) );
        }
    }
}

int solve(string s, int n){
    set<string> permutations;
    for(int i=0; i<s.length()-n+1; i++){
        bool cons = true;
        for(int j=i; j<i+n; j++){
            if(!isConsonant(s[j])) cons = false;
        }
        if(cons){
            addPermutations(i,permutations,s.length(),n);
        }
    }
    return permutations.size();
}

int main() {
    ofstream fout("codeJam.out");
    ifstream fin("codeJam.in");
    long caseNumber=0;
    fin >> caseNumber;
    for(long i=1; i<=caseNumber; i++){
        
        string s;
        int n;
        fin >> s >> n;
        
        string solution = toString(solve(s,n));
        fout << "Case #" << i << ": " << solution << endl;
        cout << "Case #" << i << ": " << solution << endl;
    }
    
    return 0;
}
