#include <cstdio>
#include <algorithm>
#include <utility>
using namespace std;

#define time first.first
#define op first.second
#define cnt second
#define EVENT(a, b, c) make_pair(make_pair((a), (b)), (c))

typedef long long ll;
typedef pair< pair<ll, int> , ll > event;
const ll mod = 1000002013LL;
const int max_m = 1000;

int n, m;
ll o[max_m], e[max_m], p[max_m];
event ev[2 * max_m];
ll cnt[2 * max_m];

ll calc(ll diff)
{
    ll res = ll(n) * diff % mod;
    res += mod - diff * (diff - 1LL) / 2LL % mod;
    res %= mod;
    return res;
}

int main()
{
    int T; scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%d %d", &n, &m);
        for(int i = 0; i < m; i++)
            scanf("%lld %lld %lld", &o[i], &e[i], &p[i]);

        ll tot = 0LL;
        for(int i = 0; i < m; i++)
            tot += calc(e[i] - o[i]) * p[i] % mod, tot %= mod;

        for(int i = 0; i < m; i++)
        {
            ev[2 * i + 0] = EVENT(o[i], -1, p[i]);
            ev[2 * i + 1] = EVENT(e[i], +1, p[i]);
        }
        sort(ev, ev + 2 * m);

        ll ans = 0LL;
        for(int i = 0; i < 2 * m; i++)
            cnt[i] = 0LL;
        for(int i = 0; i < 2 * m; i++)
        {
            if(ev[i].op == -1)
                cnt[i] += ev[i].cnt;
            else if(ev[i].op == +1)
            {
                ll pass = ev[i].cnt;
                for(int j = i - 1; j >= 0; j--)
                {
                    if(ev[j].op == -1)
                    {
                        ll out = min(pass, cnt[j]);
                        ll diff = ev[i].time - ev[j].time;
                        ans += calc(diff) * out % mod; ans %= mod;
                        pass -= out;
                        cnt[j] -= out;
                    }
                }
            }
        }

        printf("Case #%d: %lld\n", t, (tot - ans + mod) % mod);
    }
    return 0;
}
