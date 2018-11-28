#include <cstdio>

const int MAXN = 1111;

int a[MAXN];

int main() {
    int t;
    scanf("%d", &t);
    for (int cs = 1; cs <= t; ++cs) {
        int n, ans = 0;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &a[i]);
            if (a[i] > ans)
                ans = a[i];
        }
        for (int i = ans - 1; i; --i) {
            int cur = i;
            for (int j = 0; j < n; ++j)
                if (a[j] > i)
                    cur += (a[j] - i) / i + ((a[j] - i) % i > 0);
            if (cur < ans)
                ans = cur;
        }
        printf("Case #%d: %d\n", cs, ans);
    }
    return 0;
}
