#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out2.o","w",stdout);
    long long i,j,k,l,m,n,t,a;
    long long ara[12];
    scanf("%lld",&t);
    for(long long cs=1;cs<=t;cs++)
    {
        scanf("%lld",&m);
        n=m;
        a=1;
        if(n==0)
            printf("Case #%lld: INSOMNIA\n",cs);
        else
        {
            for(i=0;i<11;i++)
                ara[i]=0;
            long long c=0;
            while(c<10)
            {
                long long q=n;
                while(q>0)
                {
                    long long r=q%10;
                    q=q/10;
                    if(ara[r]==0)
                    {
                        ara[r]=1;
                        c++;
                    }

                }
                if(c==10)
                    printf("Case #%lld: %lld\n",cs,n);
                else

                    {
                        a++;
                        n=a*m;
                    }

            }
        }
    }
    return 0;
}

