//
//  main.cpp
//  codejam
//
//  Created by 李科 on 16/4/9.
//  Copyright © 2016年 李科. All rights reserved.
//

#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;

typedef long long int LL;


int dp[106][106][2];



int main(int argc, const char * argv[]) {
    
    ifstream cin("/Users/like/Downloads/B-large.in");
    ofstream cout("/Users/like/Desktop/Github/googlecodejam/codejam/codejam/B-small-attempt0.out");
    
    int t;
    cin >> t;
    string s;
    
    for (int i = 1; i <= t; i++) {
        cin >> s;
        char c = '+';
        int ans = 0;
        
        for (int j = int(s.size()) - 1; j >= 0; j--) {
            if (s[j] == c) {
                continue;
            }
            ans++;
            c = s[j];
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    
    return 0;
}
