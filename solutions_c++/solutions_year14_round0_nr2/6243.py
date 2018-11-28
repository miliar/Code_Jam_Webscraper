#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#define INF 0x3f3f3f3f
#define eps 1e-7
using namespace std;

double c,f,x,sum;
double ans;

int main()
{
    int T,t,i,j,cnt=0;
    freopen("B-large.in","r",stdin);
    freopen("output-B-large.out","w",stdout);
    while(~scanf("%d",&T))
    {
        for(t=1;t<=T;t++)
        {
            ans=INF;
            scanf("%lf%lf%lf",&c,&f,&x);
            double s=2.0;
            if(ans>x/s) ans=x/s;
            double add_t,rt=0;
            do
            {
                add_t=c/s;
                rt+=add_t;
                s+=f;
                double ntime=rt+x/s;
                //printf("%lf  %lf  %lf\n",add_t,s,ntime);
                if(ans>ntime) ans=ntime;
                else break;
            }while(add_t>eps);
            printf("Case #%d: %.7lf\n",t,ans);
        }
    }
    return 0;
}

