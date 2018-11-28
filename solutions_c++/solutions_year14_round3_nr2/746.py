//
//  main.cpp
//  Problem B
//
//  Created by Umair Akhtar on 11/05/2014.
//  Copyright (c) 2014 Umair Ahmad. All rights reserved.
//

#include<algorithm>
#include<map>
#include<iomanip>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<iostream>
#include<cstring>
#include <fstream>
#include <stack>

#define ForA(i, a, b) for(i =(a); i <=(b); ++i)
#define ForD(i, a, b) for(i = (a); i >= (b); --i)
#define For(i, b) for(i=0; i<(b); ++i)
#define pb push_back
#define peeks top()
#define peekq front()
#define peek(v) v[0]
#define last(v) v[v.size()-1]
#define SQR(a) ((a)*(a))
#define ulld unsigned long long int
#define lld long long int

using namespace std;


ulld totals;


void test(string temp) {
    vector<bool> b(255, 1);
    bool valid = true;
    int i;
    For(i, temp.size()) {
        char tee = temp[i];
        if(b[tee]) {
            while(temp [i] == tee) i++;
            b[tee] = false;
            i--;
        }
        else {
            valid = false;
            return;
        }
    }
    if(valid ) totals++;
}

void check(string p, vector<string> &sts) {
    string temp ="";
    int i;
    For(i, p.length()) {
        int in = p[i];
        in -= 48;
        temp += sts[in];
    }
    test(temp);
}

void perm(string a, string b, vector<string> &sts) {
    if(b.length() == 0) {
        check(a, sts);
        return;
    }
    for(int i=0; i<b.length(); i++) {
        perm(a+b[i], b.substr(0, i) + b.substr(i+1), sts);
    }
    
}



int main(){
    ifstream fin("Data.in");
    ofstream fout("Data.out");
    
    
    int tt;
    fin>>tt;
    int cc =0;
    while(tt--) {
        cc++;
        fout<<"Case #"<<cc<<": ";
        totals = 0;
        
        vector<string> sts;
        int s;
        fin>>s;
        int i;
        For(i, s) {
            string st;
            fin>>st;;
            sts.pb(st);
        }
        
        string pattern;
        For(i, sts.size()) {
            pattern += i+48;
        }
        perm("", pattern, sts);
        
        fout<<totals<<endl;
    }
    fin.close();
    fout.close();
    
    return 0;
}

