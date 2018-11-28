#include <iostream>
# include <cstdio>
using namespace std;

int main()
{
    //freopen("1.in","r",stdin);
    //freopen("1.out","w",stdout);

    int t;
    scanf("%d",&t);
    for(int ci = 1; ci <= t; ++ci)
    {
        double p = 2.0, k = 0.0, ans= 0.0;
        double c, f, x;
        scanf("%lf%lf%lf",&c,&f,&x);
        while( x/(p+k*f) > ( c/(p+k*f) + x/(p+k*f+f)))
        {
            ans +=  c/(p+k*f);
            k += 1.0;
        }
        ans += x/(p+k*f);
        printf("Case #%d: %.7lf\n",ci,ans);
    }
    return 0;
}
