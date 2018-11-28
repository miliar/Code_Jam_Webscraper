#include <stdio.h>
#include <algorithm>
using namespace std;
int t[210];
int n, p, q;
int h[110], v[110];
int dp[110][1010][2];
void upd(int &x, int v){
    x = max(x, v);
}
int main(){
    int T, ri = 1, k, i, j, hh, x0, y0, x1, y1;
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%d%d", &p, &q, &n);
        for (i = 0; i < n; i++) scanf("%d%d", &h[i], &v[i]);
        for (i = 0; i <= n; i++){
            for (j = 0; j < 1010; j++){
                dp[i][j][0] = dp[i][j][1] = -(1<<30);
            }
        }
        dp[0][0][0] = 0;
        for (i = 0; i < n; i++){
            k = 0; hh = h[i];
            if (p == q){
                x0 = 0;
                y0 = (hh + p - 1) / p - 1;
            }else if (p > q){
                x0 = 0;
                y0 = (hh + q - 1) / q - 1;
            }else{
                x0 = 0;
                while (hh > p && (hh % q == 0 || hh % q > p)){
                    hh -= p;
                    x0++;
                }
                y0 = (hh + q - 1) / q - 1;
            }
            int tmp = min(x0, y0);
            x0 -= tmp; y0 -= tmp;

            hh = h[i] - q;
            if (hh <= 0) x1 = -1;
            else{
                if (p == q){
                    x1 = 0;
                    y1 = (hh + p - 1) / p - 1;
                }else if (p > q){
                    x1 = 0;
                    y1 = (hh + q - 1) / q - 1;
                }else{
                    x1 = 0;
                    while (hh > p && (hh % q == 0 || hh % q > p)){
                        hh -= p;
                        x1++;
                    }
                    y1 = (hh + q - 1) / q - 1;
                }
                int tmp = min(x1, y1);
                x1 -= tmp; y1 -= tmp;
            }
            for (j = 0; j < 1010; j++){
                if (dp[i][j][0] >= 0){
                    upd(dp[i + 1][j + (h[i] + q - 1) / q][0], dp[i][j][0]);
                    if (j >= x0){
                        upd(dp[i + 1][j - x0 + y0][1], dp[i][j][0] + v[i]);
                    }
                }
                if (dp[i][j][1] >= 0){
                    if (h[i] - q <= 0){
                        upd(dp[i + 1][j][0], dp[i][j][1]);
                        int jj = (h[i] + p - 1) / p;
                        if (j >= jj){
                            upd(dp[i + 1][j - jj][1], dp[i][j][1] + v[i]);
                        }
                    }else{
                        upd(dp[i + 1][j + (h[i] - q + q - 1) / q][0], dp[i][j][1]);
                        if (j >= x1){
                            upd(dp[i + 1][j - x1 + y1][1], dp[i][j][1] + v[i]);
                        }
                    }
                }
            }
        }
        int ans = 0;
        for (j = 0; j < 1010; j++){
            ans = max(ans, dp[n][j][0]);
            ans = max(ans, dp[n][j][1]);
        }
        printf("Case #%d: %d\n", ri++, ans);
    }
    return 0;
}
