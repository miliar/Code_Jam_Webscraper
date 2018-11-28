#include<stdio.h>
int main()
{
    int ca;
     freopen("F:\\2large.in","r", stdin);
	freopen("F:\\2outlarge.txt", "w", stdout);
    scanf("%d",&ca);
    int cc=0;
    
    while(ca--)
    {
        double c,f,x;
        double t=0;
        double v=2;
        double nn=0;
        scanf("%lf%lf%lf",&c,&f,&x);
        if(c<x)
        {
            nn=c;
            t+=c/v;
        }
        else
        {
            printf("Case #%d: %lf\n",++cc,x/v);
            continue;
        }
        
        while(1)
        {
            if(( x-nn)/v>(x-nn+c)/(v+f))
            {
                v+=f;
                t+=c/v;
            }
            else
            {
                t+=(x-nn)/v;
                break;
            }

        }
        printf("Case #%d: %.7lf\n",++cc,t);
    }
    return 0;
}
