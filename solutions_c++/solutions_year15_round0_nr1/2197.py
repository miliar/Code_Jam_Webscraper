//
//  main.cpp
//  gcj1
//
//  Created by Lewnus on 15/4/11.
//  Copyright (c) 2015年 Lewnus. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

char str[2000];
int sum,ans,n,T;

int main(int argc, const char * argv[]) {
    freopen("../../../../../../../../Documents/sw_cpp/sf/gcj1/gcj1/1.in","r",stdin);
    freopen("../../../../../../../../Documents/sw_cpp/sf/gcj1/gcj1/1.out","w",stdout);
    scanf("%d",&T);
    for (int i=1;i<=T;i++){
        scanf("%d%s",&n,str);
        sum = 0;
        ans = 0;
        for (int j=0;j<=n;j++)
        {
            ans = max(ans, j-sum);
            sum += str[j]-'0';
        }
        printf("Case #%d: %d\n",i,ans);
    }

}
