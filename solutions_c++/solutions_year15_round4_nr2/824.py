#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <math.h>
using namespace std;

int main()
{
    freopen("c:\\codejam\\B-small-attempt0.in", "r", stdin);
    freopen("c:\\codejam\\B-small.out", "w", stdout);
    int Test,cas=1,N;
    double V,X;
    scanf("%d",&Test);
    while(Test--)
    {
        printf("Case #%d: ",cas++);
        cin>>N>>V>>X;
        if(N==1)
        {
            double v,T;
            cin>>v>>T;
            if(fabs(X-T) < 1e-7)
                printf("%.8lf\n",V/v);
            else
                puts("IMPOSSIBLE");
        }
        else
        {
            double v1,v2,T1,T2;
            cin>>v1>>T1>>v2>>T2;
            if(T1>T2)
            {
                swap(T1,T2);
                swap(v1,v2);
            }
            if(T1==T2&&T2==X)
            {
                double v,T;
                v = v1+v2;
                T=T1;
                if(fabs(X-T) < 1e-7)
                    printf("%.8lf\n",V/v);
                else
                    puts("IMPOSSIBLE");
            }
            else if(T1==X)
            {
                double v,T;
                v=v1;
                T=T1;
                if(fabs(X-T) < 1e-7)
                    printf("%.8lf\n",V/v);
                else
                    puts("IMPOSSIBLE");
            }
            else if(T2==X)
            {
                double v,T;
                v=v2;
                T=T2;
                if(fabs(X-T) < 1e-7)
                    printf("%.8lf\n",V/v);
                else
                    puts("IMPOSSIBLE");
            }
            else if(T1>X || T2<X)
            {
                puts("IMPOSSIBLE");
            }
            else {
            double t = (X-T2)/(T1-X);
            double k2=V/(1+t);
            double k1=V*t/(1+t);
            double ans=k1/v1;
            ans = max(ans,k2/v2);
            printf("%.8lf\n",ans);
            }
        }
    }
    return 0;
}
