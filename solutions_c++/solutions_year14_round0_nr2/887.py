#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("sout1.txt","w",stdout);
    int t,tc;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++)
    {
        double C,F,X,R=2.0;
        scanf("%lf%lf%lf",&C,&F,&X);
        double var,tim=0.0,mini=X/R,LIM=X;
        if(LIM<15000.0) LIM=15000.0;
        while(R<=LIM)
        {
            var=tim+(X/R);
            if(var<mini)
                mini=var;
            tim+=C/R;
            R+=F;
        }
        printf("Case #%d: %.9lf\n",tc,mini);
    }
    return 0;
}
