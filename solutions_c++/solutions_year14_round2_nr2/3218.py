#include<stdio.h>
int main()
{
    long long int t,a,b,k,xx,c,i,j;
    scanf("%lld",&t);
    for(xx=1;xx<=t;xx++)
    {
        c=0;
        scanf("%lld%lld%lld",&a,&b,&k);
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
                if((i&j)<k) c++;
        }
        printf("Case #%lld: %lld\n",xx,c);
    }
    return 0;
}
