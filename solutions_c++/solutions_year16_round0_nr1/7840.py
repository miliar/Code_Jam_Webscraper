#include<bits/stdc++.h>

using namespace std;

#define ll long long

map<ll,ll> m;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    ll t;
    ll i,j,k;
    ll c=0;
    scanf("%lld",&t);

    while(t--)
    {
        m.clear();
        c++;
        k=1;
        ll n,f;
        scanf("%lld",&n);

        if(n==0)
        {
            printf("Case #%lld: INSOMNIA\n",c);
            continue;
        }

        f=(k*n);

        while(1)
        {
            int flag=0;
            for(int l=0;l<10;l++)
                if(m[l]==0)
                {
                    flag=1;
                    break;
                }

            if(flag==0)
            {
                printf("Case #%lld: %lld\n",c,(f-n));
                break;
            }
            else
            {
                while(f>0)
                {
                    m[f%10]++;
                    f=f/10;
                }
            }

            k++;
            f=(k*n);
        }

    }

    return 0;
}
