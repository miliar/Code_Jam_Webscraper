#include <iostream>
#include <cstdio>
#include <cstring>

typedef __int64 i64;

using namespace std;

i64 ans[] = {0, 1, 1, 1, 2, 2, 2, 2, 2, 3};
i64 ten[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};
int num[128];

bool check(i64 x) {
    int i, j, p;

    for (p = 0; x; x /= 10) num[p++] = x % 10;
    for (i = 0, j = p - 1; i < j; ++i, --j) {
        if (num[i] != num[j]) return false;
    }

    return true;
}

i64 calc(int p, i64 a, i64 b, i64 up) {
    i64 ret = 0, cur = a * ten[p] + b ;
    int i;

    if (cur * cur <= up) ret += check(cur * cur);
    for (i = 0; i < 3; ++i) {
        cur = a * ten[p + 1] + i * ten[p] + b;
        if (cur * cur <= up) ret += check(cur * cur);
    }

    return ret;
}

i64 dfs(int p, i64 a, i64 b, i64 up) {
    i64 ret = calc(p, a, b, up), cur = a * ten[p] + b, na, nb;
    int i;

    if (cur * cur > up) return 0;
    for (i = 0; i < 3; ++i) {
        na = a * 10 + i; nb = i * ten[p] + b;
        cur = na * ten[p + 1] + nb;
        if (cur * cur <= up) ret += dfs(p + 1, na, nb, up);
    }

    return ret;
}

i64 solve(i64 x) {
    if (x < 10) return ans[x];
    return dfs(1, 1, 1, x) + dfs(1, 2, 2, x) + 3;
}

int main() {
    int t, ct = 0;
    i64 l, r;

    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);

    cin >> t;
    while (t--) {
        cin >> l >> r;
        printf("Case #%d: ", ++ct);
        cout << solve(r) - solve(l - 1) << endl;
    }

    return 0;
}
