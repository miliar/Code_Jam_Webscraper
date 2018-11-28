#include <cstdio>
#include <algorithm>
using namespace std;

int n;
int a[2048];

void read() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
    }
}

void solve() {
    int ans = 1005;
    for (int i = 1; i <= 1005; i++) {
        int cur = i;
        for (int j = 1; j <= n; j++) {
            cur += (a[j] - 1) / i;
        }
        ans = min(ans, cur);
    }
    printf ("%d\n", ans);
}

int main() {
    int i, cases;

    scanf("%d", &cases);
    for (i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        solve();
    }
    return 0;
}

