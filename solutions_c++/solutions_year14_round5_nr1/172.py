#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define MAX 1000100

using namespace std;

typedef long long i64;

i64 a[MAX], sum[MAX];

inline i64 makeData(i64 p, i64 q, i64 r, i64 s, i64 k) {
    return (k * p + q) % r + s;
}

double solve(int n, int p, int q, int r, int s) {
    int i, j, t;
    i64 x, y, z, ret = 0;

    for (sum[0] = i = 0; i < n; ++i) {
        a[i + 1] = makeData(p, q, r, s, i);
        sum[i + 1] = sum[i] + a[i + 1];
    }
    for (i = 1; i <= n; ++i) {
        t = upper_bound(sum, sum + n + 1, (sum[n] + sum[i - 1]) >> 1) - sum - 1;
        x = sum[i - 1]; y = sum[t] - x; z = sum[n] - sum[t];
        ret = max(ret, min(x + y, min(x + z, y + z)));
        if (t < n) {
            x = sum[i - 1]; y = sum[t + 1] - x; z = sum[n] - sum[t + 1];
            ret = max(ret, min(x + y, min(x + z, y + z)));
        }
    }

    return (double)ret / (double)sum[n];
}

int main() {
    int t, ct = 0, n, p, q, r, s;

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
        printf("Case #%d: %.10f\n", ++ct, solve(n, p, q, r, s));
    }

    return 0;
}
