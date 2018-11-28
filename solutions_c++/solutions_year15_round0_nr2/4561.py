#include <cstdio>
#include <queue>
#include <algorithm>
#include <memory.h>


using namespace std;

const int N = 1111;

int a[N], n, f[N][N];

int solve() {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
    }
    memset(f, 0, sizeof(f));
    sort(a, a + n);

    for (int i = 1; i <= n; ++i) {
        int val = a[i - 1];
        for (int j = 0; j <= 1000; ++j) {
            f[i][j] = val;
            for (int k = 1; k <= j; ++k) {
                f[i][j] = min(f[i][j], max(f[i - 1][j - k], (val + k) / (k + 1)));
            }
        }
    }
    int ans = f[n][0];
    for (int i = 1; i <= 1000; ++i) {
        ans = min(ans, f[n][i] + i);
    }
    return ans;
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int it = 1; it <= T; ++it) {
        printf("Case #%d: %d\n", it, solve());
    }
    return 0;
}
