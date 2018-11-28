#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

const int MOD = 1000002013;

int T, m;
ll n;
ll f[10000], t[10000], p[10000];

ll gao(ll f, ll t, ll p) {
    ll dist = t - f;
    ll cost = (n + n - dist + 1) * dist / 2;
    p %= MOD;
    cost = cost % MOD * p % MOD;
    return cost;
}

int main() {
    scanf("%d", &T);
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        scanf("%lld%d", &n, &m);
        vector<ll> xs;
        for (int i = 0; i < m; ++i) {
            scanf("%lld%lld%lld", &f[i], &t[i], &p[i]);
            xs.push_back(f[i]);
            xs.push_back(t[i]);
        }
        sort(xs.begin(), xs.end());
        xs.resize(unique(xs.begin(), xs.end()) - xs.begin());
        int N = (int)xs.size();
        vector<ll> enter(N, 0LL);
        ll res = 0;
        for (int i = 0; i < m; ++i) {
            ll cost = gao(f[i], t[i], p[i]);
            res = (res + cost) % MOD;
            f[i] = lower_bound(xs.begin(), xs.end(), f[i]) - xs.begin();
            t[i] = lower_bound(xs.begin(), xs.end(), t[i]) - xs.begin();
            enter[f[i]] += p[i];
            enter[t[i]] -= p[i];
        }
        map<ll, ll> mp;
        for (int i = 0; i < N; ++i) {
            if (enter[i] > 0) {
                mp[i] += enter[i];
            } else {
                ll total = -enter[i];
                while (total > 0) {
                    map<ll, ll>::iterator it = --mp.end();
                    if (total >= it->second) {
                        ll cost = gao(xs[it->first], xs[i], it->second);
                        total -= it->second;
                        mp.erase(it);
                        res = (res - cost) % MOD;
                    } else {
                        ll cost = gao(xs[it->first], xs[i], total);
                        it->second -= total;
                        total = 0;
                        res = (res - cost) % MOD;
                    }
                }
            }
        }
        res = (res % MOD + MOD) % MOD;
        printf("Case #%d: %lld\n", caseNum, res);
    }
    return 0;
}
