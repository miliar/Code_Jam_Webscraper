#include <iostream>
#include<stdio.h>
#define ll long long int
using namespace std;
ll count[10]={0};
int main()
{
    freopen ("xyz2.in","r",stdin);
    ll t,c=1,n;
    scanf("%lld",&t);
    while(t--)
    {
        for(ll i=0; i<10; i++) count[i]=0;
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%lld: INSOMNIA\n",c);
            c++;
        }
        else
        {
            ll i=1;
            ll x=n;
            ll xx;
            while(1)
            {
                x=n*i;
                xx=x;
                while(x!=0)
                {
                    count[x%10]++;
                    x/=10;
                }
                ll y=1;
                for(ll j=0; j<10; j++)
                {
                    if(count[j]==0)
                        {
                            y=0;
                            break;
                        }
                }
                if(y==1) break;
                i++;
            }
            printf("Case #%lld: %lld\n",c,xx);
            c++;
        }


    }
}
