#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>

using namespace std;

int main()
{
    freopen("x.in","r",stdin);
    freopen("x.txt","w",stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1 ; cas <= T ; cas++)
    {
        double c, f, x;
        scanf("%lf%lf%lf", &c, &f, &x);
        if(c >= x)
        {
            printf("Case #%d: %.7lf\n", cas, x/2);
            continue;
        }
        double maxv = f*(x-c)/c;
        int buytimes;
        if(maxv < 2.0)buytimes = 0;
        else          buytimes = floor((maxv - 2.0)/f);

        double fin = x/2;
        for(int k = 0 ; k < 2 ; k++)
        {
            buytimes += k;

            maxv = 2.0 + buytimes * f;
            double ans = x / maxv;

            for(int i = 0 ; i < buytimes ; i++)
            {
                double v = 2.0 + (double)i * f;
                double t = c / v;
                ans += t;
            }

            fin = min(ans, fin);
        }
        printf("Case #%d: %.7lf\n", cas, fin);
    }
    return 0;
}
