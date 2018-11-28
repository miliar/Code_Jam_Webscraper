#include <bits/stdc++.h>

using namespace std;

const int N = 1e5 + 5;

int dp[N];
int a[N];
int n;

int calc(int lim) {
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        cnt += (a[i] - 1) / lim;
    }
    return cnt;
}

int work() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
    }
    int ret = 1000;
    for (int i = 1; i <= 1000; i++) {
        ret = min(ret, calc(i) + i);
    }
    return ret;
}

void init() {
    freopen("B-large.in", "r", stdin);
    freopen("B_large.out", "w", stdout);
}

int main() {
    int T;
    init();
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        printf("Case #%d: %d\n", cas, work());
    }
    return 0;
}
