#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
using namespace std;

double pi=acos(-1.0);

int main()
{
    long long T,r,t;

    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%lld",&T);
    for(int ii=1;ii<=T;ii++)
    {
        scanf("%lld%lld",&r,&t);
        //t=(long long)t*1.0/pi;
        //printf("t=%lld\n",t);
        long long ll=0,rr=t;
        while(ll<rr)
        {
            long long l=(ll+rr+1)/2;
            double now=1.0*(2*r-1+2 + 2*r-1+2 +4*l-4)*l/2;
            //printf("l=%lld now=%f\n",l,now);
            if (now-1<1.0*t)
            {
                long long p=(2*r-1+2 +2*r-1+2 +4*l-4)*l/2;
                if (p<=t) ll=l;
                else rr=l-1;
            } else rr=l-1;
        }
        printf("Case #%d: %lld\n",ii,ll);
    }
    return 0;
}
