#include <bits/stdc++.h>

typedef long long int ll;

#define mod 1000000007
#define sl(x) scanf("%lld",&x)
#define s(x) scanf("%d",&x)
#define pb push_back
#define mp make_pair
#define INF 1000000000

using namespace std;

ll powr (ll a, ll b)
{
    if (b == 0)
        return 1;
    ll x = powr(a, b/2);
    if (b % 2 == 0)
        return (x*x)%mod;
    else
        return (((x*x)%mod)*a)%mod;
}

int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,p = 0;
    ll n,i;
    s(t);
    while(t--) {
        p++;
        sl(n);
        if(n == 0) {
            printf("Case #%d: INSOMNIA\n",p);
            continue;
        }
        ll tmp = n;
        int pres[10] = {};
        ll cnt = 0;
        while(tmp > 0) {
            if(pres[tmp%10] == 0) {
                pres[tmp%10] = 1;
                cnt++;
            }
            tmp /= 10;
        }
        ll x = 1;
        while(cnt < 10) {
            x++;
            tmp = n*x;
            while(tmp > 0) {
                if(pres[tmp%10] == 0) {
                    pres[tmp%10] = 1;
                    cnt++;
                }
                tmp /= 10;
            }
        }
        printf("Case #%d: %lld\n",p,n*x);
    }
    return 0;
}
