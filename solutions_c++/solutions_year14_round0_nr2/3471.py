//
//  main.cpp
//  CookieClicker
//
//  Created by 向仁楷 on 14-4-12.
//  Copyright (c) 2014年 Giraffe-Tech. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[])
{

    int i,j,k,tc,y;
    double x,c,f,ans;
    
    freopen("./B-large.in", "r", stdin);
    freopen("./B-large.out", "w", stdout);
    
    scanf("%d",&tc);
    
    for (k = 1; k <= tc; k ++) {
        scanf("%lf %lf %lf",&c,&f,&x);
        ans = 0;
        y = (f*x - 2*c) / (c*f);
        if (y < 0) {
            y = 0;
        }
        for (i = 0; i < y; i ++) {
            ans += c / (double)(2 + i*f);
        }
        ans += x / (double)(2 + y*f);
        printf("Case #%d: %.7f\n",k,ans);
    }
    
    return 0;
}

