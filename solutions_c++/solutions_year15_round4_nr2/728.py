#include<stdio.h>
int ii, n, t;
double v, x, r1, r2, c1, c2, v1, v2, t1, t2, dif, eps=0.000001;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%ld",&t);
    for (ii=1;ii<=t;ii++)
    {
        scanf("%ld %lf %lf",&n,&v,&x);
        printf("Case #%ld: ",ii);
        if (n==1)
        {
            scanf("%lf %lf",&r1,&c1);
            t1=v/r1;
            if (c1==x)
                printf("%.7lf\n",t1);
            else
                printf("IMPOSSIBLE\n");
        }
        if (n==2)
        {
            scanf("%lf %lf",&r1,&c1);
            scanf("%lf %lf",&r2,&c2);
            if (c1!=c2)
            {
                v1=(x*v-v*c2)/(c1-c2);
                v2=v-v1;
                if ((v2<0)||(v1<0))
                    printf("IMPOSSIBLE\n");
                else
                {
                    t1=v1/r1;
                    t2=v2/r2;
                    if (t1>t2)
                        printf("%.7lf\n",t1);
                    else
                        printf("%.7lf\n",t2);
                }
            }
            else
            {
                if (c1!=x)
                    printf("IMPOSSIBLE\n");
                else
                {
                    printf("%.7lf\n",v/(r1+r2));
                }
            }
        }
    }
    return 0;
}
