#include <stdio.h>
#include <string.h>
int cas, n, p, q, inp[110][2], nhi[110][2], dp[110][2010], ans;
int main() {
    scanf("%d", &cas);
    for (int iii=0; iii<cas; iii++) {
        scanf("%d%d%d", &p, &q, &n);
        for (int i=0; i<n; i++) {
            scanf("%d%d", &inp[i][0], &inp[i][1]);
            nhi[i][0] = (inp[i][0]-1) / q;
            nhi[i][1] = (inp[i][0] - nhi[i][0] * q + p - 1) / p;
            //printf("%d-%d\n", nhi[i][0], nhi[i][1]);
        }
        memset(dp, -63, sizeof(dp));
        dp[0][1] = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<2010-nhi[i][0]-1; j++) {
                dp[i+1][j+nhi[i][0]+1] = dp[i][j];
            }
            for (int j=0; j<2010; j++) {
                if (j+nhi[i][0]-nhi[i][1] >= 0 && j+nhi[i][0]-nhi[i][1] <2010) {
                    if (dp[i][j] + inp[i][1] > dp[i+1][j+nhi[i][0]-nhi[i][1]])
                        dp[i+1][j+nhi[i][0]-nhi[i][1]] = dp[i][j] + inp[i][1];
                }
            }
        }
        ans = 0;
        for (int i=0; i<2010; i++) if (ans < dp[n][i]) ans = dp[n][i];
        printf("Case #%d: %d\n", iii+1, ans);
    }
    return 0;

}
