//
//  main.cpp
//  a.cpp
//
//  Created by lianlian on 15/4/11.
//  Copyright (c) 2015年 lianlian. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int n,data[1010];

int sum[1010];

int ans = 0;

int main(int argc, const char * argv[]) {
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t = 1; t <= T; t ++){
        memset(sum,0,sizeof(sum));
        ans = 0;
        scanf("%d",&n);
        char c;
        for(int i = 0; i <= n; i ++){
            scanf(" %c",&c);
            data[i] = c - '0';
        }
        
        for(int i = 1; i <= n; i ++)
            sum[i] = sum[i-1] + data[i-1];
        for(int i = 1; i <= n; i ++)
            ans = max (ans, i - sum[i]);
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
