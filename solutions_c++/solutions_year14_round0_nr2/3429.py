#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{
    freopen("cookie-l.in","rt",stdin);
    freopen("cookie-l.out","wt",stdout);
    int i,tcase,t,k;
    double c,f,x,r,sum,tmp1,tmp2,tmp3;
    scanf("%d",&tcase);
    for(t=1;t<=tcase;t++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        r = 2.0;
        sum = 0;
        k = ceil(x/c-2.0/f-1.0);
        for(i=0;i<k;i++,r+=f)
            sum += c/r;
        sum += x/r;
        printf("Case #%d: %.7lf\n",t,sum);
    }
    return 0;
}
