//
//  main.cpp
//  FHC_Pattern
//
//  Created by Andriy Medvid on 11.01.15.
//  Copyright (c) 2015 Andriy Medvid. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

#define MAX_NUM 1000000000


//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ/Round_2/A.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ/Round_2/A.out")

#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ/Round_2/A-large.in")
#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ/Round_2/A-large.out")

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ/Round_2/A-small-attempt0.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ/Round_2/A-small-attemp0.out")

// PR -> P
// PS -> S
// RS -> R


string st1, st2, st3;

int n, p, r, s;

void OutCase(int caseNum) {
    cout << "Case #" << (caseNum+1) << ": ";
}

bool checkIsGood(string str) {
    int rc = 0, pc = 0, sc = 0;
    
    for(int i = 0; str[i]; i++){
        if(str[i] == 'R')
            rc++;
        else if(str[i] == 'P')
            pc++;
        else
            sc++;
    }
    if(rc == r && pc == p && sc == s)
    {
        cout << str;
        return true;
    }
    return false;
}

void iteration() {
    cin >> n >> r >> p >> s;
    
    st1 = "PR";
    st2 = "PS";
    st3 = "RS";
    
    for(int i = 1; i < n; i++) {
        
        string s1 = st1 + st2;
        string s2 = st1 + st3;
        string s3 = st2 + st3;
        
        st1 = s1;
        st2 = s2;
        st3 = s3;
    }
    
    if(checkIsGood(st1))
        return;
    if(checkIsGood(st2))
        return;
    if(checkIsGood(st3))
        return;
    
    cout << "IMPOSSIBLE";
}

int main(int argc, const char * argv[]) {
    
    freopen(IN_NAME, "r", stdin);
    freopen(OUT_NAME, "w", stdout);
    
    int T;
    
    cin >> T;
    
    for(int tIter = 0; tIter < T; tIter++) {
        
        
        OutCase(tIter);
        
        iteration();
        
        cout << endl;
    }
    
    return 0;
}


