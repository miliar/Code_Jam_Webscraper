#include <stdio.h>

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,t;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        double ans=x/2.0;
        double cnt=0;
        for(int i=0;;i++)
        {
            cnt+= c/(2.0+i*f);
            double tmp=cnt+x/(2.0+(i+1)*f);
            if(ans>tmp) ans=tmp;
            else break;
        }
        printf("%lf\n",ans);
    }
    return 0;
}
