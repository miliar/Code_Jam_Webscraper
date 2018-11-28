#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <cmath>
main()
{
    int T, i, a, b, j, p1[5][5], p2[5][5], ans, num=0, v, n;
    double c, f, x, speed, t;
    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d", &T);
    while(T--)
    {
        scanf("%lf %lf %lf", &c, &f, &x);
        speed=2;
        printf("Case #%d: ", ++num);
        if(x<=c)
        {
            printf("%.7lf\n",x/2);
        }
        else
        {
            t=0;
            n=ceil(x/c-1-2/f);
            for(i=1; i<=n; i++)
            {
                t+=c/speed;
                speed+=f;
            }
            t+=x/speed;
            printf("%.7lf\n", t);
        }

    }

    return 0;
}
