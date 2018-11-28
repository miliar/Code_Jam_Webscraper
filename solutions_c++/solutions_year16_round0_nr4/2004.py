//
//  main.cpp
//  CodeJam
//
//  Created by WanTangtang on 16/4/9.
//  Copyright © 2016年 WanTangtang. All rights reserved.
//

//#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
//    printf("sha");
    int t, k, c, s;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++)
    {
        scanf("%d%d%d", &k, &c, &s);
        if((k+c-1)/c > s) printf("Case #%d: IMPOSSIBLE\n", i);
        else
        {
            int temp = (k+c-1)/c;// the number of tiles that need to see
            printf("Case #%d:", i);
            long long int res = 0;
            int cur = k-1;
            while(temp--)
            {
                res = 0;
                long long int weight = 1;
                for(int i = 0 ; i < c; i++)
                {
                    res += cur * weight;
                    weight *= k;
                    if(cur > 0) cur--;
                }
                printf(" %lld", res+1);
            }
            printf("\n");
        }
    }
    return 0;
}
