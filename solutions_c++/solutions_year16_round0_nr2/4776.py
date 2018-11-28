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
    //freopen("testdata.in", "r", stdin);
    clock_t clk = clock();
#endif
    int caseCnt;
    scanf(" %d",&caseCnt);
    for(int d = 1;d <= caseCnt;d++){
        cin >> str;
        n = str.size();
        memset(dp, 0, sizeof(dp));
        printf("Case #%d: ",d);
        if(str[0] == '-') dp[0][0] = 0,dp[0][1] = 1;
        else dp[0][0] = 1,dp[0][1] = 0;
        for(int i = 1; i < n;i++){
            if(str[i] == '-') {
                dp[i][0] = dp[i-1][0];
                dp[i][0] = min(dp[i][0],dp[i-1][1]+1);
                dp[i][1] = dp[i-1][1] + 2;
                dp[i][1] = min(dp[i][1],dp[i-1][0]+1);
            }else{
                dp[i][0] = dp[i-1][1] + 1;
                dp[i][0] = min(dp[i][0],dp[i-1][0]+2);
                dp[i][1] = dp[i-1][1];
                dp[i][1] = min(dp[i][1],dp[i-1][0]+1);
            }
        }
        printf("%d\n",dp[n-1][1]);
    }
    return 0;
}
