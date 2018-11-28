#include <cstdio>
#include <cstring>

#define ll long long int

using namespace std;

ll T, C=1;
ll R[1024], r;

ll inv(ll n) {
    ll r=0;
    while (n) {
        ll d = n%10ll;
        n /=10ll;
        r = 10ll*r + d;
    }
    return r;
}

ll qnts(ll n) {
    ll c = 0;
    for (ll i =0; i< r;i++)
        if (R[i] <= n) c++;
    return c;
}

int main() {

    r = 0;
    for (ll i=1;i*i<=110000000000000ll;i++) if (inv(i)==i) {
        ll t = i*i;
        if (inv(t)==t) {
            R[r++] = i*i;
        }
    }

/*    for (ll i=0;i<r;i++)
        printf("%lld **= %lld\n",R[i],R[i]*R[i]);*/

    for(scanf("%lld",&T);T--;) {
        printf("Case #%lld: ",C++);
        ll a, b;
        scanf("%lld %lld",&a,&b);
        printf("%lld\n",qnts(b) - qnts(a-1));
    }

    return 0;
}
