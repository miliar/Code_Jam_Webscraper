#include<stdio.h>
int main()
{
    double divisor;
    double achieving[2];
    double producing[2];
    double total[2];
    double x,f,c,min;
    int t,i,j;
    scanf("%d",&t);
    int count=1;
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        divisor=2.0;
        achieving[0]=0;
        producing[0]=x/divisor;
        total[0]=achieving[0]+producing[0];
        min=total[0];
        for(j=1; ;j++)
        {
            i=j%2;
            achieving[i]=achieving[1-i]+c/divisor;
            divisor+=f;
            producing[i]=x/divisor;
            total[i]=achieving[i]+producing[i];
            if(total[i]<=min)
              min=total[i];
            else
                break;
        }
        printf("Case #%d: %lf\n",count,min);
        count++;
    }
    return(1);
}
