#include <cstdio>
#include <algorithm>

int a[10000];

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        int n, X;
        scanf("%d%d", &n, &X);
        for (int i = 0; i < n; ++ i)
            scanf("%d", &a[i]);
        std :: sort(a, a + n);
        int ans = n;
        for (int i = n; i >= 0; -- i) {
            bool flag = true;
            for (int j = 0, k = i - 1; j < k; ++ j, -- k)
                if (a[j] + a[k] > X) {
                    flag = false;
                    break;
                }
            if (flag) {
                ans = n - i + (i + 1) / 2;
                break;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
