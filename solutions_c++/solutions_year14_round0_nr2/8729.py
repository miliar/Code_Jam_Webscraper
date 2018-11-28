#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>

using namespace std;

double c,f,x;

double eps = 0.0000001;

double findMin(double hasNow, double perSecCookie)
{
    double cur = 0.0;
    while(hasNow < x)
    {
        double toBuyRem = (x - hasNow) / perSecCookie;
        double toBuyFarm = (c - hasNow) / perSecCookie;
        if(toBuyFarm + x/(perSecCookie + f) < toBuyRem)
        {
            perSecCookie += f;
            cur += toBuyFarm;
            hasNow = 0.0;
        }
        else
        {
            cur += toBuyRem;
            hasNow += (x - hasNow);
        }
    }
    return cur;
}

int main(void)
{
    int T;
    freopen("B-large.in","r", stdin);
    freopen("B-large.out","w", stdout);
    scanf("%d",&T);
    for(int t = 0; t<T; t++)
    {
        double perSecCookie = 2.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        double ans = findMin(0.0,perSecCookie);

        printf("Case #%d: ", t+1);
        printf("%lf\n", ans);
    }
    return 0;
}
