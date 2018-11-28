#include<stdio.h>
long long power(long long n,long long r)
{
    if(r==0) return 1;
    if(r%2==0)
    {
        long long y=power(n,r/2);
        return y*y;
    }
    return n*power(n,r-1);
}
int main()
{
 //   freopen("input.in","r",stdin);
  //  freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int l=0;
    while(l<t)
    {
        l++;
        long long k,c,s;
        scanf("%lld%lld%lld",&k,&c,&s);
        int i;
        printf("Case #%d: ",l);
        for(i=0;i<k;i++)
        {
            printf("%lld ",1+i*power(k,c-1));
        }
        printf("\n");
    }
    return 0;
}
