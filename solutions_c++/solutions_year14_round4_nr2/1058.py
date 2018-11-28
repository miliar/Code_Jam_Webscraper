//
//  main.cpp
//  GCJ
//
//  Created by 祝风翔 on 14-5-11.
//  Copyright (c) 2014年 祝风翔. All rights reserved.
//

#include <iostream>
#include <memory.h>
#include <stdio.h>
#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <queue>
#include <math.h>
#include <algorithm>
#include <set>
using namespace std;
typedef long long LL;
vector<pair<int,int>>E;
int inv[1000 + 5],iny[1000 + 5];
int dp[1000 + 5][1000 + 5];
void update(int i,int j,int v) {
    if(dp[i][j] == -1) dp[i][j] = v;
    else {
        dp[i][j] = min(dp[i][j],v);
    }
    return;
}
int main(){
    int t,cas = 0;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small-attempt0.out","w",stdout);
    while(t--) {
        int n;
        scanf("%d",&n);
        //printf("%d\n",n);
        E.clear();
        memset(inv,0,sizeof(inv));
        memset(iny,0,sizeof(iny));
        for(int i = 0;i < n;i++) {
            int tmp;
            scanf("%d",&tmp);
            E.push_back(make_pair(tmp,i));
        }
        sort(E.begin(),E.end());
        for(int i = 0;i < n;i++) {
            for(int j = i + 1;j < n;j++) {
                if(E[j].second > E[i].second) {
                    inv[i]++;
                }else iny[i]++;
            }
        }
        memset(dp,-1,sizeof(dp));
        dp[0][0] = 0;
        for(int i = 0;i < n - 1;i++) {
            for(int j = 0;j <= i;j++) {
                int l = j,r = i - j;
                if(dp[l][r] == -1) continue;
                int cur = n-2-i;
                update(l,r+1,dp[l][r] + inv[cur]);
                update(l+1,r,dp[l][r] + iny[cur]);
            }
        }
        int ans = -1;
        for(int j = 0;j <= n - 1;j++) {
            if(dp[j][n-1-j] != -1){
                if(ans == -1 || dp[j][n-1-j] < ans)
                    ans = dp[j][n-1-j];
            }
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}