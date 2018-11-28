//
//  GCJQA.cpp
//  playground
//
//  Created by 張正昊 on 9/4/2016.
//  Copyright © 2016 Adam Chang. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <set>
#include <stack>
#include <cmath>
#include <map>
#include <complex>

using namespace std;

string str;
int n;
int dp[105][2];

int main(){
#ifndef ONLINE_JUDGE
    freopen("testdata.in", "r", stdin);
#endif
    int caseCnt;
    scanf(" %d",&caseCnt);
    for(int d = 1;d <= caseCnt;d++){
        printf("Case #%d:",d);
        long long k,c,s;
        cin >> k >> c >> s;
        long long kc = 1;
        for(int i = 1; i< c; i++){
            kc *= k;
        }
        long long cur = 1;
        vector<long long> pos;
        for(int i = 1; i <= s; i++){
            if (cur > kc*k) {
                break;
            }
            pos.push_back(cur);
            cur += kc;
        }
        sort(pos.begin(), pos.end());
        pos.erase(unique(pos.begin(), pos.end()), pos.end());
        for(int i = 0 ; i < pos.size(); i++){
            cout << ' ' << pos[i];
        }
        puts("");
    }
    return 0;
}
