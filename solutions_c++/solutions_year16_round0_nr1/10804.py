#include<bits/stdc++.h>
using namespace std;

#define ll long long

ll T,N,number[1000005];
int main()
{
    freopen("inputt.txt","r",stdin);
    freopen("output.txt","w",stdout);

    ll i;
    for(ll k=1;k<=1000000;k++)
    {
        ll arra[11]={0};
        for( i=1;;i++)
        {
            ll n=k*i;
            while(n)
            {
                ll r=n%10;
                n/=10;
                arra[r]=1;
            }
            ll c=0;
            for(ll j=0;j<10;j++)
            {
                if(arra[j]==1)
                    c++;
            }
            if(c==10)
                break;
        }
        number[k]=k*i;
    }

    scanf("%lld",&T);
    for(ll tt=1;tt<=T;tt++)
    {
        scanf("%lld",&N);
        if(N==0)
        printf("Case #%lld: INSOMNIA\n",tt);
        else
        printf("Case #%lld: %lld\n",tt,number[N]);

    }
    return 0;
}
