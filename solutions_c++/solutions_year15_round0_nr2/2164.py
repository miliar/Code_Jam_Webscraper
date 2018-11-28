#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    for (int k = 1; k <= n; ++k) {
        int m;
        scanf("%d", &m);
        int a[1024];
        int max = 0;
        for (int i = 0; i < m; ++i) {
            scanf("%d", &a[i]);
            if (a[i] > max)
                max = a[i];
        }
        for (int ans = 1; ans < max; ++ans) {
            int ret = ans;
            for (int i = 0; i < m; ++i) {
                if (a[i] > ans) {
                    ret += (a[i] - 1) / ans;
                }
            }
            if (ret < max)
                max = ret;
        }
        printf("Case #%d: %d\n", k, max);
    }
    return 0;
}
