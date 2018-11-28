#include <cstdio>
#include <algorithm>

int a[1000];
bool use[1000];

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++ i)
            scanf("%d", &a[i]);
        std :: fill(use, use + n, false);
        int ans = 0;
        while (n > 0) {
            int idx = -1;
            for (int i = 0; i < n; ++ i)
                if (!use[i] && (-1 == idx || a[i] < a[idx]))
                    idx = i;
            use[idx] = true;
            ans += std :: min(idx, n - idx - 1);
            for (int i = idx; i < n - 1; ++ i) {
                a[i] = a[i + 1];
                use[i] = use[i + 1];
            }
            -- n;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
