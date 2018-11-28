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
//B-small-attempt0
#define IN_NAME ("B-small-attempt2.in")
#define OUT_NAME ("B-small-attempt2.out")

void OutCase(int caseNum) {
    cout << "Case #" << (caseNum+1) << ": ";
}

int main(int argc, const char * argv[]) {
    
    freopen(IN_NAME, "r", stdin);
    freopen(OUT_NAME, "w", stdout);
    
    int n;
    vector<int> nums;
    
    int T;
    
    cin >> T;
    
    for(int tIter = 0; tIter < T; tIter++) {
        
        cin >> n;
        int a;
        nums.clear();
        
        for(int i = 0; i < n; i ++) {
            cin >> a;
            nums.push_back(a);
        }
        
        int mn = 1000;
        for(int i = 1; i <= 1000; i++) {
            int res = 0;
            for(int j = 0; j < nums.size(); j++)
                res += (nums[j] - 1) / i;
            mn = min(mn, res + i);
        }
        
        OutCase(tIter);
        // out answer
        cout << mn;
        
        cout << endl;
    }
    
    return 0;
}


