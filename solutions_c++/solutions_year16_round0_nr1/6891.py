
#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    freopen("A-large.in","rt",stdin);
freopen("outputhitesh.cpp","wt",stdout);
    long long t,k=1;
    scanf("%lld",&t);
    while(t--)
    {
        long long n,a[11];
        for(int i=0;i<=10;i++)a[i]=0;
        scanf("%lld",&n);
        long long x=n,f=0,j=2,d=n;
        if(n==0)
            printf("Case #%lld: INSOMNIA\n",k++);
        else
        while(1)
        {
            f=0;
            long long tempX=x;
            while(tempX!=0)
            {
                long long y=tempX%10;
                a[y]=1;
                tempX=tempX/10;
            }
            for(int i=0;i<10;i++)
           {
            if(a[i]==0)
            {
                f=1;break;
            }
           }
            if(f==0)
                {
                    printf("Case #%lld: %lld\n",k++,d);
                break;

                }
            else
            {
                x=n*j;
                j++;
               // printf("%d\n",x);
                //break;
            }
            d=x;
        }
    }
    return 0;
}
