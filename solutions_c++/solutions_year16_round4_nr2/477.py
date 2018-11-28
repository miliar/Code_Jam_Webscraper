#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
double p[2000];
int sel[2000];
double ans = 0;
double f[201][201];
double check() {
    memset(f, 0, sizeof f);
    f[0][0] = 1;
    for (int i = 1; i <= sel[0]; i++) {
        f[i][0] = f[i - 1][0] * (1 - p[sel[i]]);
        for (int j = 1; j <= i; j++) {
            f[i][j] =
                f[i - 1][j - 1] * (p[sel[i]]) + f[i - 1][j] * (1 - p[sel[i]]);
        }
    }
    return f[sel[0]][sel[0] / 2];
}
int n, k;
void solve() {
    if (k > n) return;
    if (k % 2 != 0) return;
    sort(p + 1, p + 1 + n);
    for (int i = 0; i <= k; i++) {
        sel[0] = k;
        for (int j = 1; j <= i; j++) sel[j] = j;
        for (int j = 1; j <= k - i; j++) sel[j + i] = n - j + 1;
        ans = max(ans, check());
    }
}
int main() {
    int cas;
    scanf("%d", &cas);
    for (int _ = 1; _ <= cas; _++) {
        scanf("%d%d", &n, &k);
        for (int i = 1; i <= n; i++) scanf("%lf", &p[i]);
        ans = 0;
        solve();
        printf("Case #%d: %.8f\n", _, ans);
    }
}
