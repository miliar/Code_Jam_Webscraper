//
//  main.cpp
//  problem
//
//  Created by zhangchenxu1 on 15/4/11.
//  Copyright (c) 2015年 zhangchenxu1. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
int a[1010];
int main()
{
    freopen("/Users/zhangchenxu1/Desktop/input.txt","r",stdin);
    freopen("/Users/zhangchenxu1/Desktop/output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int cas=1;
    while(T--)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d",&a[i]);
        int ans=1000;
        for(int i=1;i<=1000;i++)
        {
            int temp=0;
            for(int j=0;j<n;j++)
            {
                temp+=(a[j]+i-1)/i-1;
            }
            temp+=i;
            ans=min(ans,temp);
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    
}
