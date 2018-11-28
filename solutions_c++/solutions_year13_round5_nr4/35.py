#include <stdio.h>
double dp[1<<20];
char c[30];
int main(){
    int T, ri = 1, k, i, j, n, x;
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%s", c);
        x = 0;
        for (i = 0; c[i]; i++){
            if (c[i] == '.') x |= (1<<i);
        }
        n = i;
        for (k = 1; k <= x; k++){
            dp[k] = 0;
            for (i = 0; i < n; i++){
                int d = n;
                for (j = i; j < n; j++){
                    if (k & (1<<j)){
                        dp[k] += dp[k ^ (1<<j)] + d;
                        break;
                    }
                    d--;
                }
                if (j == n){
                    for (j = 0; j < i; j++){
                        if (k & (1<<j)){
                            dp[k] += dp[k ^ (1<<j)] + d;
                            break;
                        }
                        d--;
                    }
                }
            }
            dp[k] /= n;
        }
        printf("Case #%d: %.12f\n", ri++, dp[x]);
    }
    return 0;
}
