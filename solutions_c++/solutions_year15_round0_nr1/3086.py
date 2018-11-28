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
        int temp;
        scanf("%1d",&temp);
        int ans=0;
         for(int i=1;i<=n;i++)
        {
            int t;
            scanf("%1d",&t);
            if(temp<i)
            {
                ans+=i-temp;
                temp=i;
            }
            temp+=t;
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    
}
