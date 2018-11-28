#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cctype>

using namespace std;

typedef long long ll;

#define MAXN 1024

int n, m;
ll ans, ori;
map<ll,ll> t, p;

int main () {
    int casos;
    scanf ("%d", &casos);

    const ll MOD = 1000002013;

    for (int caso = 1; caso <= casos; ++caso) {
        printf ("Case #%d: ", caso);

        t.clear();
        p.clear();
        scanf ("%d %d", &n, &m);

        ori = 0;
        for (int i = 0; i < m; ++i) {
            ll x, y, qt;
            scanf ("%lld %lld %lld", &x, &y, &qt);

            if (t.find(x) != t.end()) t[x] += qt;
            else t[x] = qt;

            if (p.find(y) != p.end()) p[y] += qt;
            else p[y] = qt;

            ll a = n - (y - x) + 1;
            ll s = (((n + a) % MOD * (y - x) % MOD) * 500001007) % MOD;
            ll tmp = (qt * s) % MOD;
            ori = (ori + tmp) % MOD;
        }

        ans = 0;
        for (map<ll,ll>::iterator i = p.begin(); i != p.end(); ++i) {
            ll to = i->first, qt = i->second;

            while (qt > 0) {
                map<ll,ll>::iterator it = t.lower_bound(to);
                if (it == t.end() || it->first != to) --it;
                ll from = it->first, disp = it->second;

                ll tmp = min(qt, disp);
                qt -= tmp;
                it->second -= tmp;

                if (it->second == 0) t.erase(it);

                ll a = n - (to - from) + 1;
                ll s = (((n + a) % MOD * (to - from) % MOD) * 500001007) % MOD;
                tmp = (tmp * s) % MOD;
                ans = (ans + tmp) % MOD;
            }
        }

        printf ("%lld\n", (ori - ans + MOD) % MOD);
    }

    return 0;
}

