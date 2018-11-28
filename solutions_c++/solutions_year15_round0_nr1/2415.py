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

#define IN_NAME ("A-small-attempt0.in")
#define OUT_NAME ("A-small-attempt0.out")

void OutCase(int caseNum) {
    cout << "Case #" << (caseNum+1) << ": ";
}

int main(int argc, const char * argv[]) {
    
    freopen(IN_NAME, "r", stdin);
    freopen(OUT_NAME, "w", stdout);
    
    int T;
    
    cin >> T;
    
    for(int tIter = 0; tIter < T; tIter++) {
        
        int maxShyness;
        char str[1010];
        int sum = 0;
        int mx = 0;
        
        cin >> maxShyness;
        cin >> str;
        
        for(int i = 0; i <= maxShyness; i++)
        {
            mx = max(mx, i - sum);
            sum += str[i] - '0';
        }
        
        OutCase(tIter);
        // out answer
        cout << mx;
        
        cout << endl;
    }
    
    return 0;
}


