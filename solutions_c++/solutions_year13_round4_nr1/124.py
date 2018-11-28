#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const ll P = 1000002013ll;

ll n;

ll cost(ll len) {
    return (len * (n - len + 1 + n) / 2) % P;
}

int m;
ll l[1010], r[1010], p[1010];

struct event {
    ll x, p;
    bool f;

    event() {x = p = f = 0;}
    event(ll _x, ll _p, bool _f) {x = _x, p = _p, f = _f;}

    bool operator <(const event & a) const {
        if (x != a.x) return x < a.x;
        return f < a.f;
    }
};

event e[2010];

event st[2010];
int sz;

ll sum, sum2;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d ", &T);
    forn(t, T) {
        printf("Case #%d: ", t + 1);

        cin >> n >> m;
        sum = 0;
        forn(i, m) {
            cin >> l[i] >> r[i] >> p[i];
            sum = (sum + (cost(r[i] - l[i]) * p[i]) % P) % P;
            e[2 * i] = event(l[i], p[i], 0);
            e[2 * i + 1] = event(r[i], p[i], 1);
        }

        sort(e, e + 2 * m);
        sz = 0;
        sum2 = 0;
        forn(i, 2 * m)
            if (e[i].f) {
                while (e[i].p != 0) {
                    ll dp = min(e[i].p, st[sz - 1].p);
                    sum2 = (sum2 + (cost(e[i].x - st[sz - 1].x) * dp) % P) % P;
                    e[i].p -= dp;
                    st[sz - 1].p -= dp;
                    while (sz > 0 && st[sz - 1].p == 0)
                        sz--;
                }
            } else
                st[sz++] = e[i];
        printf("%lld\n", (sum - sum2 + P) % P);
    }
    return 0;
}
