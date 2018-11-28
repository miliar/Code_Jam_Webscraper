#include<stdio.h>
#include<math.h>
main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        long long int n,r,t,c;
        scanf("%lld%lld",&r,&t);
        c=r-r*r-2*t;//printf("%lld %lld\n",c,(long long )sqrt(1-4*c));
        n=(-1+(long long)sqrt(1-4*c))/2;
        printf("Case #%d: ",cas++);
        printf("%lld\n",(n-r+1)/2);
    }
    return 0;
}
