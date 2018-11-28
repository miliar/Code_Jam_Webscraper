//
//  main.cpp
//  noob
//
//  Created by Lingsong Zeng on 2/29/16.
//  Copyright © 2016 Lingsong Zeng. All rights reserved.
//


#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        printf("Case #%d: ",++cas);
        long long n;
        cin>>n;
        if(n==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        int mark[15]={0};
        int cnt=0;
        long long a=1;
        while(1)
        {
            long long tmp=a*n;
            while(tmp)
            {
                if(!mark[tmp%10])
                    cnt++;
                mark[tmp%10]=true;
                tmp/=10;
            }
            if(cnt>=10)
                break;
            a++;
        }
        printf("%lld\n",a*n);
    }
}