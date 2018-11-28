#include<stdio.h>
#define EPS 0.0000001
int main()
{
    int t,k;
    double c,f,x,current,total;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        if(x<c)
        {
            printf("Case #%d: %.7lf\n",k,(x/2.0));
            continue;
        }
        current=2.0;
        total=0.0;
        while(1)
        {
            double y=x/current;
            double z=(c/current)+(x/(current+f));
            if(y<z)
            {
                total+=y;
                break;
            }
            else
            {
                total+=(c/current);
                current+=f;
            }
        }
        printf("Case #%d: %.7lf\n",k,total);
    }
    return 0;
}
