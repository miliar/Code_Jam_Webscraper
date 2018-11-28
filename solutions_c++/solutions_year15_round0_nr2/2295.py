#include <cstdio>
#include <cstring>
#include <iostream>

#define _N 0x1000
#define INF 1000000000

using namespace std;

int n, p[_N];

int cost(int v) {
    int ret = 0;
    for (int i = 0; i < n; ++i) {
        ret += (p[i] + v - 1) / v - 1;
    }
    return ret + v;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++cas) {
        int r = 0;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &p[i]);
            r = max(r, p[i]);
        }

        int ans = INF;
        for (int i = 1; i <= r; ++i) {
            ans = min(ans, cost(i));
        }
        printf("Case #%d: %d\n", cas, ans);
    }

    return 0;
}
