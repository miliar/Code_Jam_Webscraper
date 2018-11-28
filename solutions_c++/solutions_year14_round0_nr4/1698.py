//
//  main.cpp
//  mmmmm
//
//  Created by zhou yi on 14-4-10.
//  Copyright (c) 2014年 edward. All rights reserved.
//

#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

double a[1010];
double b[1010];

int main()
{
    int t,c=0;
    scanf("%d",&t);
    while (c++,t--)
    {
        int n;
        scanf("%d",&n);
        for (int i = 0; i < n; ++ i)
        {
            scanf("%lf",&a[i]);
        }
        for (int i = 0; i < n; ++ i)
        {
            scanf("%lf",&b[i]);
        }
        sort(a, a+n);
        sort(b, b+n);
        int ansNormal = 0;
        int l=0,r=n-1;
        for (int i = n-1; i >= 0; -- i)
        {
            if (a[i] > b[r])
            {
                ansNormal ++;
                l++;
            }
            else
                r--;
        }
        int ansDeceit = 0;
        l = 0;
        r = n-1;
        for (int i = n-1; i >= 0; -- i)
        {
            if (b[i] > a[r])
                l++;
            else
            {
                ansDeceit ++;
                r--;
            }
        }
        printf("Case #%d: ",c);
        printf("%d %d\n",ansDeceit,ansNormal);
    }
    return 0;
}