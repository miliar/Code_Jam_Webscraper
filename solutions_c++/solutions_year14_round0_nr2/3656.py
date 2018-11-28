#include<bits/stdc++.h>
#define LIM 100000
using namespace std;
double cost[LIM];
int main()
{
    int tc,t;
    freopen("B-large.in","r",stdin);
    scanf("%d",&tc);
    for(t = 1 ; t<= tc ; t++)
    {
        int i;
        double f,c,x;
        double rate = 2.0000000;
        double tt = 0.000000;
        double mn = 100000000.0000;
        scanf("%lf %lf %lf",&c,&f,&x);
        for(i = 1 ; i<=LIM ; i++)
        {
            cost[i - 1] = (tt + x/rate)/1.0000000;
            tt = tt + c/rate;
            rate = rate + f;
           if(mn > cost[i-1])// > 0.0000000001 )
           mn = cost[i-1];
        }
        printf("Case #%d: %0.7lf\n",t,mn);
    }
    return 0;
}

