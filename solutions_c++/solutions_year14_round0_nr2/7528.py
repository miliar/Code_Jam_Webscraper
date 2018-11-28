//
//  main.cpp
//  B
//
//  Created by Ji Zhou on 14-4-12.
//  Copyright (c) 2014年 Ji Zhou. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int t;
double v,c,f,x;

int main(int argc, const char * argv[])
{
    freopen("1.txt", "r", stdin);
    freopen("1.out", "w", stdout);
    scanf("%d",&t);
    for (int test=1;test<=t;test++)
    {
        printf("Case #%d: ",test);
        v=2.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        double time=c/v;
        while ((x-c)/v+time>time+x/(v+f))
        {
            v+=f;
            time+=c/v;
            //printf("%.7lf\n",time);
        }
        time+=(x-c)/v;
        printf("%.7lf\n",time);
    }
    return 0;
}