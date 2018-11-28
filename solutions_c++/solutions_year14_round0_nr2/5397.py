#include <stdio.h>

int main()
{
    freopen("B1.in","r",stdin);
    freopen("B.out","w",stdout);
    int i,j,n,T,cnt=1;
    double c,f,x;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        double ans=x/2;
        double v=2;
        double cost=0;
        while(1)
        {
            double tmp=c/v;
            v=v+f;
            cost=cost+tmp;
            double t=cost+x/v;
            if (t<ans) ans=t;
            else break;
        }
        printf("Case #%d: %lf\n",cnt++,ans);
    }
    return 0;

}
