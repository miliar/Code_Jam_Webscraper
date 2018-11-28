#include<bits/stdc++.h>
#define  mx            12
#define  clr(a)        memset(a, 0, sizeof(a))

using namespace std;
typedef long long int ll;

ll a[mx];

int main()
{
    freopen("A-large (2).in","r",stdin);
    freopen("out.txt", "w", stdout);
    ll t, cas, n;
    ll num;
    cin>>t;
    for(cas = 1; cas<=t; cas++)
    {
        cin>>n;
        clr(a);
        ll cnt = 1;
        if(n == 0)
        {
            printf("Case #%lld: INSOMNIA\n", cas);
            continue;
        }
        int sz = 0;
        while(1)
        {
            ll m = n;
            m *= cnt;
            num = m;
            cnt++;
            while(m != 0)
            {
                ll rem = m%10;
                if(!a[rem])
                {
                    //cout<<rem<< " "<<num<<endl;
                    a[rem] = 1;
                    sz++;
                }
                m /= 10;
            }
            if(sz == 10)
            {
                printf("Case #%lld: %lld\n", cas, num);
                break;
            }
        }
    }
    return 0;
}
