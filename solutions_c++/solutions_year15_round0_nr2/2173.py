#include <cstdio>
#include <cstdlib>
#include <cstring>

int a[1010];

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int n;
        scanf("%d", &n);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &a[i]);
            if (a[i] > ans)
                ans = a[i];
        }
        int max = ans;
        for (int i = max; i > 0; --i) {
            int tmp = i;
            for (int j = 0; j < n; ++j) {
                tmp += (a[j] - 1) / i;
            }
            if (tmp < ans)
                ans = tmp;

        }
        printf("Case #%d: %d\n", t, ans);
    }

    return 0;
}
