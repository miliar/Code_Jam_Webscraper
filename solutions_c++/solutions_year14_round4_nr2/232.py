#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>

#define MAX 100010
#define X first
#define Y second
#define LB(x) ((x) & -(x))

using namespace std;

typedef pair<int, int> Pii;

struct BIT {
    int c[MAX], sz;

    void init(int n) {
        memset(c, 0, sizeof(c));
        sz = n;
    }

    void update(int k, int v) {
        for ( ; k <= sz; k += LB(k)) c[k] += v;
    }

    int query(int k) const {
        int ret = 0;
        for ( ; k; k -= LB(k)) ret += c[k];
        return ret;
    }
} bit;

int a[MAX], b[MAX];
Pii x[MAX];

int solve(int n) {
    int m, p, d = 0, ret = 0, i;

    for (i = 0; i < n; ++i) x[i] = make_pair(a[i], i);
    sort(x, x + n);
    bit.init(n);
    for (i = 0; i < n; ++i) {
        p = lower_bound(x, x + n, make_pair(a[i], -1)) - x + 1;
        b[i] = bit.query(p - 1);
        bit.update(p, 1);
    }
    for (i = 0; i < n; ++i) {
        p = x[i].Y - b[x[i].Y];
        if (p < n - i - 1 - p) {
            ret += p;
        } else {
            ret += n - i - 1 - p; ++d;
        }
    }

    return ret;
}

int main() {
    int t, ct = 0, n, x, i;

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (i = 0; i < n; ++i) scanf("%d", &a[i]);
        printf("Case #%d: %d\n", ++ct, solve(n));
    }

    return 0;
}
