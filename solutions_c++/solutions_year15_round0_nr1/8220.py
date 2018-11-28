//
//  main.cpp
//  test
//
//  Created by Giorgi Pataraia on 11.04.15.
//  Copyright (c) 2015 Giorgi Pataraia. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main(int argc, const char * argv[]) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int t;
    cin >> t;
    
    for (int i = 0 ; i < t ; i ++) {
        int smax;
        cin >> smax;
        int clapping = 0;
        int required = 0;
        for (int j = 0 ; j < smax + 1; j++) {
            char c;
            cin >> c;
            int curRC = c - '0';
            if (j == 0) {
                clapping = curRC;
            }
            else {
                if (j > clapping) {
                    required += j - clapping;
                    clapping += j - clapping;
                }
                clapping += curRC;
            }
        }
        
        cin.clear();
        printf("Case #%d: %d\n", i + 1, required);
    }
    
    
    return 0;
}
