//#include<bits/stdc++.h>
#include <iostream>   // std::cout
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
using namespace std;

bool canMake (int i, int a[26]) {
    string names[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    for(int j=0 ; j < names[i].size() ; j++) {
        if (a[names[i][j]-'A'] > 0) {
            a[names[i][j]-'A']--;
        }
        else {
            for(int k=0 ; k < j ; k++)
                a[names[i][k]-'A']++;
            return false;
        }
    }
    return true;
}
void print(int a[26]) {
    for (int i=0 ; i < 26 ; i++) {
        cout<< a[i] <<" ";
    }
    cout << endl;
}
string solve (string s) {
    int a[26];
    memset(a, 0 ,sizeof a);
    for (int i =0 ; i < s.size() ; i++) {
        a[s[i]-'A']++;
    }
    stringstream res;
    int seq[10] = {0, 2, 4, 6, 8, 5, 3, 7, 9, 1};
    for(int i = 0 ; i<10 ; i++) {
        //print(a);
        if (canMake(seq[i], a)) {
            res << seq[i];
            //cout << ">> " << seq[i] <<endl;
            //print(a);
            i--;
        }
    }
    string result = res.str();
    sort (result.begin(), result.end());
    return result;
}

int main() {
    int kases;
    cin >> kases;
    int i=1;
    while (kases) {
        string s;
        cin >> s;
        cout << "Case #" << i << ": " << solve(s) << endl;
        i++;
        kases--;
    }
    return 0;
}
