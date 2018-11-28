#include <cstdio>
#include <cstring>

using namespace std;

int d[1005];
int cnt[1005];

int main() {
    int T, n;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d", &n);
        int dmax = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", &d[i]);
            if (d[i] > dmax) dmax = d[i];
        }
        int ans = dmax * n;
        for (int i = 1; i <= dmax; i++) {
            int cur = i;
            memset(cnt, 0, sizeof(cnt));
            for (int j = 0; j < n; j++) {
                if (d[j] <= i) continue;
                cur += (d[j] - 1) / i;
            }
            if (cur < ans) ans = cur;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
