//
//  main.cpp
//  noob
//
//  Created by Lingsong Zeng on 2/29/16.
//  Copyright © 2016 Lingsong Zeng. All rights reserved.
//


#include<string>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        printf("Case #%d:",++cas);
        int k,c,s;
        cin>>k>>c>>s;
        long long tmp=1;
        for(int i=1;i<c;i++)
            tmp*=k;
        long long ans=1;
        for(int i=1;i<=s;i++)
        {
            printf(" %lld",ans);
            ans+=tmp;
        }
        printf("\n");
    }
}