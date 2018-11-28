//
//  main.cpp
//  codejam
//
//  Created by shawpan on 4/12/14.
//  Copyright (c) 2014 shawpan. All rights reserved.
//
#include <iostream>

int main(int argc, const char * argv[])
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i;
    long double c,f,x,h,r,ans;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        
        scanf("%Lf%Lf%Lf",&c,&f,&x);
        h = c > x ? x :c;
        r = 2.0;
        ans = h / r;
        
        while(h < x) if(((x-h) / r) > (x / (r+f)))
        {
            r += f;
            h = c;
            ans += (c / r);
        }
        else
        {
            ans += ((x-h) / r);
            break;
        }
        
        printf("Case #%d: %.7Lf\n",i,ans);
    }
    return 0;
}

