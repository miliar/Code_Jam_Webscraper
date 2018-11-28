#include <cstdio>
#include <algorithm>

using namespace std;

int dp[1001][1000];

int main() {
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        int d, p[2000], psum = 0;
        scanf("%d", &d);
        for (int i = 0; i < d; i++) {
            scanf("%d", &p[i]);
            psum += p[i];
        }

        for (int i = 0; i < d; i++) {
            for (int k = 0; k < psum; k++) {
                dp[i+1][k] = 1000 * 1000;
            }
            for (int j = 0; j < p[i]; j++) {
                for (int k = 0; k < psum; k++) {
                    int a = max(dp[i][k], (p[i]+j)/(j+1));
                    dp[i+1][k+j] = min(dp[i+1][k+j], a);
                }
            }
        }

        int ans = 1000*1000;
        for (int i = 0; i < psum; i++) {
            ans = min(ans, i+dp[d][i]);
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
