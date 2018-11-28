#include<stdio.h>
int main()
{
    long test;
    scanf("%ld",&test);
    long i=1;
    while(i<=test)
    {
        long long x,y=0;
        long j=1;
        scanf("%lld",&x);
        int a[10]={0};
        int count=0;
        if(x==0)
        printf("Case #%ld: INSOMNIA\n",i);
        else
        {
            while(1)
            {
                y=j*x;
                while(y>0)
                {
                    if(a[y%10]==0)
                    {
                        a[y%10]=1;
                        count++;
                    }
                    y/=10;
                }
                if(count==10)
                {
                    printf("Case #%ld: %lld\n",i,j*x);
                    break;
                }
                j++;
            }
        }
        i++;
    }
    return 1;
}
