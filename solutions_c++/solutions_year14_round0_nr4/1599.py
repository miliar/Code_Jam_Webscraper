#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using std::sort;
const int MAXN = 1024;
double a[MAXN], b[MAXN];
void solve() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
        scanf("%lf", a + i);
    for (int i = 0; i < n; ++i)
        scanf("%lf", b + i);
    sort(a, a + n);
    sort(b, b + n);
    int ans0 = 0, ans1 = 0;
    for (int i = n - 1, j = n - 1, k = 0; i >= k && j >= 0; ) {
        if (a[i] > b[j]) {
            --i, --j, ++ans0;
        } else {
            ++k, --j;
        }
    }
    for (int i = n - 1, j = n - 1, k = 0; i >= 0 && j >= k; ) {
        if (a[i] > b[j]) {
            ++ans1;
            --i, ++k;
        } else {
            --i, --j;
        }
    }
    printf("%d %d\n", ans0, ans1);
    return;
}

int main() {
    int T;
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdin);
    scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        printf("Case #%d: ", t + 1);
        solve();
    }
}