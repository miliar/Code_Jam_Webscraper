#include <stdio.h>
#include <string.h>
#include <algorithm>
#define MOD  1000000007
int cas, m, n, ans, len[1010], srt[1010], maxl, nn[1010][110], col[1010], nc;
long long cnt, dp[30][110], cob[1010][1010], fac[1010], mul;
char inp[1010][110];
bool cmp(int a, int b) {
    return strcmp(inp[a]+1, inp[b]+1) < 0;
}
bool stc(char*a, char*b, int l) {
    for (int i=0; i<l; i++) if (a[i] != b[i]) return 0;
    return 1;
}
int main() {
    scanf("%d", &cas);
    for (int i=0; i<=1000; i++) {
        cob[i][0] = 1;
        cob[i][i] = 1;
    }
    for (int i=0; i<=1000; i++) {
        for (int j=1; j<i; j++) cob[i][j] = (cob[i-1][j] + cob[i-1][j-1]) % MOD;
    }
    fac[0] = 1;
    for (int i=1; i<=1000; i++) fac[i] = (fac[i-1] * i) % MOD;
    for (int ii=0; ii<cas; ii++) {
        scanf("%d%d", &m, &n);
        maxl = 0;
        for (int i=0; i<m; i++) {
            scanf("%s", inp[i]+1);
            len[i] = strlen(inp[i]+1)+1;
            srt[i] = i;
            if (maxl < len[i]) maxl = len[i];
        }
        std::sort(srt, srt+m, cmp);
        memset(nn, -1, sizeof(nn));
        ans = 0;
        cnt = 1;
        for (int i=maxl-1; i>=0; i--) {
            char lasc[1010]={-1};
            int sta, num, flg, rem;
            for (int j=0; j<=m; j++) {
                if (j!=m && len[srt[j]] <= i) continue;
                if (j==m ||lasc[0] == -1 ||!stc(inp[srt[j]]+1, lasc, i)) {
                    if (lasc[0] != -1) {
                        //printf ("%d %d %d\n", i, j, num);
                        ans += num > n ? n : num;
                        if (num >= n) {
                            nc = 0;
                            rem = num;
                            for (int k=sta; k < j; k++) {
                                if (nn[srt[k]][i+1] != -1) {
                                    col[nc++] = nn[srt[k]][i+1];
                                    rem -= nn[srt[k]][i+1];
                                }
                            }
                            flg = 1;
                            for (int k=0; k<nc; k++) {
                                if (col[k] >= n) flg = 0;
                            }
                            if (flg) {
                                memset(dp, 0, sizeof(dp));
                                dp[0][0] = 1;
                                for (int k=0; k<nc; k++) {
                                    for (int l=0; l<=n; l++) {
                                        for (int p=l; p<=n && p <= l+col[k]; p++) {
                                            dp[k+1][p] += ((dp[k][l] * cob[l][l+col[k]-p]%MOD)
                                                           * cob[n-l][p-l]%MOD) * fac[col[k]] %MOD;
                                            dp[k+1][p] %= MOD;
                                        }
                                    }
                                }
                                for (int k=0; k<rem; k++) {
                                    for (int l=n; l>0; l--) {
                                        dp[nc][l] = (dp[nc][l-1] * (n - l + 1) + dp[nc][l] * l)%MOD;
                                    }
                                    dp[nc][0] = 0;
                                }
                                cnt = (cnt * dp[nc][n] ) % MOD;
                                //printf ("%lld\n", dp[nc][n]);
                            } else {
                                mul = 1;
                                for (int k=0; k<nc; k++) {
                                    if (col[k] < n) mul = (mul * cob[n][col[k]] %MOD ) * fac[col[k]] % MOD;
                                }
                                for (int k=0; k<rem; k++) {
                                    mul = mul * n % MOD;
                                }
                                //printf ("%lld\n", mul);
                                cnt= cnt * mul % MOD;
                            }
                        }
                        nn[srt[sta]][i] = num;
                    }
                    if (j != m) {
                        strcpy(lasc, inp[srt[j]]+1);
                        sta = j;
                        num = 0;
                    }
                }
                num ++;
            }
        }
        printf ("Case #%d: %d %lld\n", ii+1, ans, cnt%MOD);
        //for (int i=0; i<m; i++) printf("%s\n", inp[srt[i]]+1);
        //if (cnt > 50000) {
        //    for (int i=0; i<m; i++) printf("%s\n", inp[srt[i]]+1);
        //    break;
        //}
    }
    return 0;
}