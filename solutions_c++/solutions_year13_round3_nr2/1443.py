#include<stdio.h>
int main()
{
    long long t,x,y,i,j;
    scanf("%lld",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%lld%lld",&x,&y);
        printf("Case #%lld: ",i);
        if(x<0)
        for(j=x;j<0;j++)
        printf("EW");
        if(x>0)
        for(j=x;j>0;j--)
        printf("WE");
        if(y<0)
        for(j=y;j<0;j++)
        printf("NS");
        if(y>0)
        for(j=y;j>0;j--)
        printf("SN");
        printf("\n");
    }
    return 0;
}
