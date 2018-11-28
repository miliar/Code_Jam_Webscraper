#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t,ca=1;
    double c,f,x,r,time;
    scanf("%d",&t);
    while(t--)
    {
        r = 2.0;
        time = 0.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        while((c+((x*r)/(r+f)))<x)
        {
            time+= c/r;
            r+= f;
        }
        time+= x/r;
        printf("Case #%d: %.7lf\n", ca++, time);
    }
    return 0;
}
