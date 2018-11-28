#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
#define N 1000000


int main()
{
    int T;
    scanf("%d",&T);

    for(int ca=1;ca<=T;ca++)
    {
       double c,f,x;
       double t=0,ans=0,r=2;
       scanf("%lf%lf%lf",&c,&f,&x);
       printf("Case #%d: ",ca);

       if(x<=c) {printf("%.7lf\n",x/r); continue;}

        t=x/r;
        double t0=0;
        for(int i=0;i<N;i++)
        {
            t0+= c/(r+i*f);
            double t1=t0 + (x-c)/(r+f*i);
            if(t1>t) break;
            else t=t1;
        }

        printf("%.7lf\n",t);
    }
    return 0;
}
