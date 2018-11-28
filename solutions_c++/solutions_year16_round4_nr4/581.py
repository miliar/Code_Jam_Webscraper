#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

char buf[30];
int n;
int g[30][30];
int h[30][30];
int a[30], flag[30];

int go(int idx) {
    if (idx == n)
        return 1;
    int i = a[idx], ok = 0;
    for (int j = 0; j < n; j++) {
        if (h[i][j] && !flag[j]) {
            ok = 1;
            flag[j] = 1;
            if (!go(idx+1))
                return 0;
            flag[j] = 0;
        }
    }
    return ok;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%s", buf);
            for (int j = 0; j < n; j++)
                g[i][j] = buf[j] - '0';
        }
        int ans = 1 << n;
        for (int mask = 0; mask < 1 << (n*n); mask++) {
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    h[i][j] = mask >> (i * n + j) & 1;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    h[i][j] |= g[i][j];
            for (int i = 0; i < n; i++)
                a[i] = i;
            int fail = 0;
            do {
                for (int i = 0; i < n; i++)
                    flag[i] = 0;
                if (!go(0)) {
                    fail = 1;
                    break;
                }
            } while (next_permutation(a, a+n));
            if (fail) continue;
            int cnt = 0;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    cnt += h[i][j] - g[i][j];
            ans = min(ans, cnt);
        }
        printf("Case #%d: %d\n", t, ans);
    }
}
