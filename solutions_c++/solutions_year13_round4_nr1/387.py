#include "iostream"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "vector"
#include "queue"
#include "stack"
#include "cmath"
#include "string"
#include "cctype"
#include "map"
#include "iomanip"
#include "set"
#include "utility"
using namespace std;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long
#define ull unsigned long long
const int inf = 1 << 29;
const double dinf = 1e30;
const ll linf = 1LL << 55;

const ll MOD = 1000002013LL;
const int N = 1111;
ll sum, ans;
int n, m;

struct Node {
    int s, t, p;
    bool operator<(const Node &x) const {
        return t < x.t;
    }
}d[N * 20];

ll cnt[N << 2];
int b[N << 2], tot;

ll calc(int o, int e, ll s) {
    if (o == e) return 0;
    ll res = e - o;
    res = ((res * (n + n + 1 - res)) / 2) % MOD;
    return (res * s) % MOD;
}

ll solve() {
    ll ans = 0;
    sort(d, d + m);
    sort(b, b + tot);
    tot = unique(b, b + tot) - b;
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < m; i++) {
        cnt[lower_bound(b, b + tot, d[i].s) - b] += d[i].p;
    }
    for (int i = 0; i < m; i++) {
        int l = lower_bound(b, b + tot, d[i].s) - b;
        int r = lower_bound(b, b + tot, d[i].t) - b;
        ll num = d[i].p;
        for (int j = r; j >= 0 && num; j--) {
            ll tmp = min(num, cnt[j]);
            ans = (ans + calc(b[j], b[r], tmp)) % MOD;
            cnt[j] -= tmp;
            num -= tmp;
        }
        if (num > 0) {
            ans = (ans + calc(d[i].s, d[i].t, num)) % MOD;
            cnt[l] -= num;
        }
    }
    ans = ((sum - ans) % MOD + MOD) % MOD;
    return ans;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("aout.in", "w", stdout);
    int T, Case = 1;
    cin >> T;
    while (T--) {
        cin >> n >> m;
        sum = tot = 0;
        for (int i = 0; i < m; i++) {
            cin >> d[i].s >> d[i].t >> d[i].p;
            b[tot++] = d[i].s;
            b[tot++] = d[i].t;
            if (d[i].s != d[i].t) {
                ll dist = d[i].t - d[i].s;
                ll tmp = (dist * (n * 2 + 1 - dist) / 2) % MOD;
                sum = (sum + tmp * d[i].p) % MOD;
            }
        }
        ll ans = solve();
        printf("Case #%d: ", Case++);
        cout << ans << endl;
    }
    return 0;
}
