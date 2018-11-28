#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX 100010

using namespace std;

int a[MAX], v[MAX];

int solve(int n, int x) {
    int ret = 0, i;

    memset(v, 0, sizeof(v));
    for (i = 0; i < n; ++i) ++v[a[i]];
    for (i = x; i > (x >> 1); --i) {
        if (v[i]) {
            ret += v[i]; v[x - i] -= v[i];
        }
    }
    for (i = (x >> 1); i; --i) {
        if (v[i] < 0) v[i - 1] += v[i];
        else if (v[i] > 0) {
            ret += ((v[i] + 1) >> 1);
            v[i - 1] -= (v[i] & 1);
        }
    }

    return ret;
}

int main() {
    int t, ct = 0, n, x, i;

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &n, &x);
        for (i = 0; i < n; ++i) scanf("%d", &a[i]);
        printf("Case #%d: %d\n", ++ct, solve(n, x));
    }

    return 0;
}
