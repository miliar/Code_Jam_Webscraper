//
//  main.cpp
//  gcj2
//
//  Created by Lewnus on 15/4/11.
//  Copyright (c) 2015年 Lewnus. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int sum ,ans ,n,T;
int a[2000];

int main(int argc, const char * argv[]) {
    freopen("../../../../../../../../Documents/sw_cpp/sf/gcj2/gcj2/1.in","r",stdin);
   freopen("../../../../../../../../Documents/sw_cpp/sf/gcj2/gcj2/1.out","w",stdout);
    scanf("%d",&T);
    for (int i=1;i<=T;i++){
        scanf("%d",&n);
        for (int j=1;j<=n;j++) scanf("%d",a+j);
        
        ans = 1000;
        
        for (int j = 1;j<=1000;j++){
            sum = 0;
            for (int k= 1;k<=n;k++)
                sum+=(a[k]-1)/j;
            sum += j;
            ans = min(ans,sum);
        }
        printf("Case #%d: %d\n",i,ans);
    }
    
}
