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

#define IN_NAME ("4.in")
#define OUT_NAME ("4.out")

void OutCase(int caseNum) {
    cout << "Case #" << (caseNum+1) << ": ";
}

int main(int argc, const char * argv[]) {
    
    freopen(IN_NAME, "r", stdin);
    freopen(OUT_NAME, "w", stdout);
    
    int T;
    
    cin >> T;
    
    for(int tIter = 0; tIter < T; tIter++) {
        
        int x, r, c;
        
        cin >> x >> r >> c;
        
        bool win = false;
        
        if(x == 1)
            win = true;
        else if(x == 2 && ((r*c)%2 == 0))
            win = true;
        else if(x == 3 && ((r*c)%3 == 0) && r > 1 && c > 1)
            win = true;
        else if(x == 4 && (r*c >= 12))
            win = true;
        
        OutCase(tIter);
        // out answer
        
        if(win)
            cout << "GABRIEL";
        else
            cout << "RICHARD";
        
        cout << endl;
    }
    
    return 0;
}


