#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>

#define MAX 16

using namespace std;

int mul[MAX], cnt[MAX], ans[MAX], tot;

int calc(int &n, int k) {
    int ret;
    for (ret = 0; !(n % k); n /= k) ++ret;
    return ret;
}

int main() {
    int t, ct = 0, r, n, m, k, cur, i, j;

    srand(time(0));

    freopen("C-small-1-attempt1.in", "r", stdin);
    freopen("C-small-1-attempt1.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        printf("Case #%d:\n", ++ct);
        scanf("%d %d %d %d", &r, &n, &m, &k);
        while (r--) {
            memset(cnt, 0, sizeof(cnt));
            for (i = 0; i < k; ++i) scanf("%d", &mul[i]);
            for (i = 0; i < k; ++i) {
                cur = mul[i];
                for (j = m; j > 1; --j) cnt[j] = max(cnt[j], calc(cur, j));
            }
            for (tot = 0, i = m; i > 1; --i) {
                for (j = 0; j < cnt[i]; ++j) ans[tot++] = i;
            }
            while (tot < n) ans[tot++] = rand() % (m - 1) + 2;
            for (i = 0; i < tot; ++i) printf("%d", ans[i]);
            printf("\n");
        }
    }

    return 0;
}
