
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#define eps 1e-8
#define db double
#define rt return
#define cn const
#define op operator
#define N 110
using namespace std;

double r[N],c[N];

int sig(double x){
  rt (x>eps)-(x<-eps);
}
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    scanf("%d",&T);

    for(int ca=1;ca<=T;ca++)
    {
        int n;
        double v,x;
        scanf("%d%lf%lf",&n,&v,&x);

        for(int i=0;i<n;i++)
             scanf("%lf%lf",&r[i],&c[i]);


        printf("Case #%d: ",ca);
        if(n==1)
        {
            if(sig(c[0]-x)==0)
            {
                double t=v/r[0];
                printf("%.9lf\n",t);
            }
            else puts("IMPOSSIBLE");
        }
        else{
            if(sig(c[0]-x)*sig(c[1]-x)>0)
                     puts("IMPOSSIBLE");
            else{
                    double t=0;

                if(sig(c[0]-x)==0 && sig(c[1]-x)==0)
                {
                    t=v/(r[0]+r[1]);
                }
                else{
                    double t1=v*(x-c[0])/(r[1]*(c[1]-c[0]));
                    double t0=(v-r[1]*t1)/r[0];
                    t=max(t1,t0);
                }

              printf("%.9lf\n",t);

            }
        }

    }
    return 0;
}

