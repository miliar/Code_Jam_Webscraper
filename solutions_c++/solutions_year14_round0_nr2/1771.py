#include <stdio.h>
#include <string.h>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,l=1,i;
    double c,x,f,min,k,value,sum;
    scanf("%d",&t);
    while(l<=t)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        min=x/2;value=2;k=c/2;
        for(i=1;;i++)
        {
            sum=0;
            value+=f;
            sum=sum+x/value+k;
            k=k+c/value;
            if(sum>=min)
            break;
            else
            min=sum;
        }
        printf("Case #%d: %.7lf\n",l++,min);
    }
    return 0;
}
