#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define MAX 2048
#define INF 0x3F3F3F3F3F3F3F3FLL

using namespace std;

typedef long long i64;

i64 s[MAX], x[MAX];
int l[MAX], r[MAX], p[MAX];

inline i64 calc(i64 n, int l, int r, i64 c) {
    return ((2 * n - x[r] + x[l] + 1) * (x[r] - x[l])) * c / 2;
}

i64 solve(int n, int m) {
    int i, j, k, tot = 0, a, b;
    i64 cur, sa = 0, sb = 0, ss;

    x[tot++] = n;
    for (i = 0; i < m; ++i) {
        x[tot++] = l[i]; x[tot++] = r[i];
    }
    sort(x, x + tot);
    tot = unique(x, x + tot) - x;
    memset(s, 0, sizeof(s));
    for (i = 0; i < m; ++i) {
        a = lower_bound(x, x + tot, l[i]) - x;
        b = lower_bound(x, x + tot, r[i]) - x;
        sa += calc(n, a, b, p[i]);
        for (j = a; j < b; ++j) s[j] += (i64)p[i];
    }

    while (1) {
        for (ss = i = 0; i < tot - 1 && s[i] == 0; ++i);
        if (i == tot - 1) break;
        for (i = 0; i < tot - 1; i = j) {
            cur = INF;
            for (j = i ; j < tot - 1 && s[j] > 0; ++j) cur = min(cur, s[j]);
            ss += calc(n, i, j, cur);
            for (k = i; k < j; ++k) s[k] -= cur;
            for ( ; j < tot - 1 && s[j] == 0; ++j);
        }

        if (ss == 0) break;
        sb += ss;
    }

    return sa - sb;
}

int main() {
    int t, ct = 0, n, m, i;

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);


    scanf("%d", &t);
    while (t--) {
        scanf("%d %d", &n, &m);
        for (i = 0; i < m; ++i) scanf("%d %d %d", &l[i], &r[i], &p[i]);
        printf("Case #%d: ", ++ct);
        cout << solve(n, m) << endl;
    }

    return 0;
}
