//
//  main.cpp
//  mmmmm
//
//  Created by zhou yi on 14-4-10.
//  Copyright (c) 2014Äê edward. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

int main()
{
    int t,xx=0;
    scanf("%d",&t);
    while(t--)
    {
        xx++;
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        double speed = 2;
        double ti = 0;
        double ans = x / speed;
        while(1)
        {
            double temp = x / speed;//printf("%lf %lf %lf %lf\n",ti,c/speed,temp,ans);
            temp += ti;
            if(temp > ans)
                break;
            else
                ans = temp;
            ti += c / speed;
            speed += f;
        }
        printf("Case #%d: ",xx);
        printf("%.7lf\n",ans);
    }
    return 0;
}
