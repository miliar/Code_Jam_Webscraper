#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long ll;

ll qps, ps[100000];

ll a, b;
int qsn;
char sn[128];

bool check() {
    for (int i = 0, j = qsn-1; i < j; i++, j--)
        if (sn[i] != sn[j])
            return 0;
    return 1;
}

void pre() {
    ll n, m;
    for (ll i = 1; i < 10000; i++) {
        n = i, m = i/10;
        while (m) {
            n = n*10 + m%10;
            m /= 10;
        }
        n *= n;
        m = n;
        qsn = 0;
        while (m) {
            sn[qsn++] = '0' + (m % 10);
            m /= 10;
        }
        sn[qsn] = 0;
        if (check())
            ps[qps++] = n;

        n = m = i;
        while (m) {
            n = n * 10 + m%10;
            m /= 10;
        }
        n *= n;
        m = n;
        qsn = 0;
        while (m) {
            sn[qsn++] = '0' + (m % 10);
            m /= 10;
        }
        sn[qsn] = 0;
        if (check())
            ps[qps++] = n;
    }
    sort(ps, ps+qps);
}

int main() {
    int T;
    int aa, bb, lo, hi;
    pre();
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%lld %lld", &a, &b);
        lo = 0, hi = qps-1;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (ps[mid] < a)
                lo = mid + 1;
            else
                hi = mid;
        }
        aa = lo;
        lo = 0, hi = qps-1;
        while (lo < hi) {
            int mid = (lo + hi + 1) >> 1;
            if (ps[mid] > b)
                hi = mid - 1;
            else
                lo = mid;
        }
        bb = lo;
        ll ans = bb - aa + 1;
        printf("Case #%d: %lld\n", t, ans);
    }
}
