#include <iostream>
#include <cstdio>
#include <cstring>
#include <iomanip>
using namespace std;

const double small=1e-8;

int main()
{
    int t,kase;
    double C,F,X,time,rate;
    scanf("%d",&t);
    for(kase=1;kase<=t;kase++)
    {
        time=0.0;
        rate=2.0;
        scanf("%lf%lf%lf",&C,&F,&X);
        while(X/rate-C/rate-X/(rate+F)>small)
        {
            time+=C/rate;
            rate+=F;
        }
        time+=X/rate;
        printf("Case #%d: %.7lf\n",kase,time);
    }
    return 0;
}
