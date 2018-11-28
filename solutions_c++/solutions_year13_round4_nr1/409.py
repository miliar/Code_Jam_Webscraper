#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iterator>
#include <numeric>
using namespace std;

#define rep(i, n)       rep2 (i, 0, n)
#define rep2(i, m, n)   for  (int i = (int)(m); i < (int)(n); ++i)
#define iter(c)         __typeof((c).begin())
#define foreach(it, c)  for (iter(c) it = (c).begin(); it != (c).end(); ++it)

typedef long long ll;

const ll mod = 1000002013;

ll t, n, m, o, e, p;

ll price(ll dist) {
    return (dist * (2 * n - dist + 1) / 2) % mod;
}

int main()
{
    cin >> t;
    rep (caseno, t) {
        ll exp = 0, opt = 0;
        map<ll, ll> ent, sur;
        
        cin >> n >> m;
        rep (i, m) {
            cin >> o >> e >> p;
            ent[o] += p;
            sur[e] += p;
            exp += price(e - o) * p;
            exp %= mod;
        }
        
        foreach (it, sur) {
            e = it->first;
            p = it->second;
            iter(ent) jt = --ent.upper_bound(it->first);
            while (p > 0 && jt != ent.begin()) {
                ll x = min(p, jt->second);
                opt += price(e - jt->first) * (x % mod);
                opt %= mod;
                p -= x;
                jt->second -= x;
                --jt;
            }
            if (p > 0) {
                opt += price(e - jt->first) * (p % mod);
                opt %= mod;
                jt->second = 0;
            }
        }
        
        cout << "Case #" << caseno + 1 << ": " << (exp - opt + mod) % mod << endl;
    }
}
