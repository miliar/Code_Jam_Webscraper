#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll a[20];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt","w", stdout);
    int t,cs=1;
    scanf("%d",&t);

    while(t--)
    {
        ll n;
        scanf("%lld",&n);

        memset(a, 0 ,sizeof a);

        printf("Case #%d: ",cs++);
        if(n==0)
        {
            printf("INSOMNIA\n");
            continue;
        }

        ll x=n;
        while(1)
        {
            ll m=n;

            while(m)
            {
                a[m%10]=1;
                m/=10;
            }
            int fl=1;
            for(int i=0; i<10; i++)
            {
//                printf("%d %lld %lld\n",i, n, a[i]);
                if(a[i]==0)
                {
                    fl=0;
//                    break;
                }
            }
            if(fl) break;
            n+=x;
        }
        printf("%lld\n",n);
    }
}

