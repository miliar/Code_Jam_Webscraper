#include <iostream>
#include <cstdio>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

#define i64 long long

int sgn(double x)
{
    if(x>1e-10) return 1;
    if(x<-1e-10) return -1;
    return 0;
}

double C,F,X;


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    int i;
    for(i=1;i<=T;i++)
    {
        scanf("%lf%lf%lf",&C,&F,&X);

        double ans=X/2;
        double v=2;
        double preTime=0;
        int j;
        for(j=1;j<=2000000;j++)
        {
            double tmp=preTime+X/v;
            if(sgn(ans-tmp)==1) ans=tmp;
            preTime+=C/v;
            v+=F;
        }

        printf("Case #%d: %.10lf\n",i,ans);
    }
}


/*

1
1 10 2

*/

