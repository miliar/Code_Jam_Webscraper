#include<cstdio>
int t,a;
double c,f,x,fx=2,lasthome=0,lastsum,nowx;
int main()
{
    scanf("%d",&t);
    for(a=1;a<=t;a++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        fx=2;
        lasthome=0;
        lastsum=x/fx;
        while(1)
        {
            lasthome+=(c/fx);
            fx+=f;
            nowx=x/fx;
            if(lasthome+nowx>=lastsum)
            {
                printf("Case #%d: %.7lf\n",a,lastsum);
                break;
            }
            lastsum=lasthome+nowx;
        }
    }
}
