//
//  b.cpp
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

int D,data[1010];

int sum[1010];

int ans = 0x7fffffff;

int maxn = 0;

int main(int argc, const char * argv[]) {
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t = 1; t <= T; t ++){
        ans = 0x3f3f3f3f;
        maxn = 0;
        D = 0;
        memset(data,0,sizeof(data));
        scanf("%d",&D);
        for(int i = 1; i <= D; i ++){
            scanf(" %d",&data[i]);
            maxn = max(maxn,data[i]);
        }
        int count = 0;
        for(int i = 1; i <= maxn; i ++){
            count = i;
            for(int j = 1; j <= D; j ++)
                if(data[j] > i){
                    if(data[j]%i == 0)
                        count += data[j]/i-1;
                    else
                        count += data[j]/i;
                }
            ans = min(ans,count);
            
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
