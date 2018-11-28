#include "stdio.h"
#include "stdlib.h"
int seen[11];
void reset()
{
    for(int i=0;i<11;i++)
        seen[i]=0;
}
void view(long long num)
{
    if(seen[num%10]==0)
    {
        seen[num%10]++; seen[10]++;
    }
    if(num>9) view(num/10);
}
main()
{
    freopen("A-Large.in","r",stdin);
    freopen("A-L.txt","w",stdout);
    int t,r;
    long long n,i;
    scanf("%d",&t);
    for(r=1;r<=t;r++)
    {
        scanf("%lld",&n);
        printf("Case #%d: ",r);
        if(n==0) printf("INSOMNIA\n");
        else
        {
            reset();
            i=0;
            while(seen[10]<10)
            {
                i++;
                view(n*i);
            };
            printf("%lld\n",n*i);
        }
    }
}
