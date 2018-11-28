#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define N 5005
#define MOD 1000002013
#define LL long long

struct Seg {
    int l, r, c;
    void read() {
        scanf("%d %d %d", &l, &r, &c);
    }
};

int n, m;
int x[N], xn;
Seg a[N];
int d[N];

inline void update(int & ret, int v) {
    ret += v;
    if (ret >= MOD) ret -= MOD;
}

inline int cal(int l, int r, int p) {
    LL ret = r - l;
    ret = (n + n - ret + 1) * ret / 2 % MOD;
    ret = ret * p % MOD;
    return (int)ret;
}

int solve() {
    int ans = 0;
    scanf("%d %d", &n, &m);
    xn = 0;
    for (int i = 0; i < m; ++i) {
        a[i].read();
        x[xn++] = a[i].l;
        x[xn++] = a[i].r;
        update(ans, cal(a[i].l, a[i].r, a[i].c));
    }
    //printf(" ans : %d\n", ans);
    sort(x, x + xn);
    xn = unique(x, x + xn) - x;
    fill(d, d + xn, 0);
    for (int i = 0; i < m; ++i) {
        int l = lower_bound(x, x + xn, a[i].l) - x;
        int r = lower_bound(x, x + xn, a[i].r) - x;
        for (int j = l; j < r; ++j)
            update(d[j], a[i].c);
    }
    for (int i = 0; i < xn; ) {
        //for (int k = 0; k < xn; ++k) printf(" %d", d[k]); puts("");
        while (0 == d[i] && i < xn) ++i;
        if (i == xn) break;
        int delta = d[i], j;
        for (j = i + 1; j < xn && d[j] > 0; ++j)
            delta = min(delta, d[j]);
        update(ans, MOD - cal(x[i], x[j], delta));
        for (int k = i; k < j; ++k)
            d[k] -= delta;
    }
    return ans;
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: %d\n", ++cas, solve());
    }
    return 0;
}
