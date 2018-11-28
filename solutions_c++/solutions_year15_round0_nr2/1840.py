#include <cstdio>
#include <cstring>

int Test, D, P[1010];

int main() {
    scanf("%d", &Test);
    for (int T = 1; T <= Test; ++T) {
        scanf("%d", &D);
        for (int i = 0; i < D; ++i) scanf("%d", P + i);
        int ans = 1e9;
        for (int t = 1; t <= 1000; ++t) {
            int cnt = t;
            for (int i = 0; i < D; ++i) {
                cnt += (P[i] - 1) / t;
            }
            if (cnt < ans) ans = cnt;
        }
        printf("Case #%d: %d\n", T, ans);
    }
}
