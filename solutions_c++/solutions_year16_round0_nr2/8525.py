#include <cstdio>
#include <cstring>

const int maxn = 107;
const int INF = 100000007;
char in[maxn];

int dp[maxn][2];
int vis[maxn][2];

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int test_case;
    scanf("%d", &test_case);
    int case_num = 1;
    while (test_case--) {
        memset(in, 0, sizeof(in));
        scanf("%s", in);
        int length = strlen(in);
        dp[0][0] = 0;
        dp[0][1] = 0;
        for (int i = 1; i <= length; i++) {
            dp[i][0] = dp[i][1] = INF;
            if (in[i - 1] == '+') {
                if (dp[i - 1][0] < dp[i - 1][1] + 1) {
                    dp[i][0] = dp[i - 1][0];
                }
                else {
                    dp[i][0] = dp[i - 1][1] + 1;
                }
                if (dp[i - 1][0] + 1 < dp[i - 1][1] + 2) {
                    dp[i][1] = dp[i - 1][0] + 1;
                }
                else {
                    dp[i][1] = dp[i - 1][1] + 2;
                }
            }
            else {
                //dp[i- 1][0]
                if (dp[i - 1][1] + 1 < dp[i - 1][0] + 2) {
                    dp[i][0] = dp[i - 1][1] + 1;
                }
                else {
                    dp[i][0] = dp[i - 1][0] + 2;
                }

                if (dp[i - 1][0] + 1 < dp[i - 1][1]) {
                    dp[i][1] = dp[i - 1][0] + 1;
                }
                else {
                    dp[i][1] = dp[i - 1][1];
                }
            }
        }
        printf("Case #%d: %d\n", case_num, dp[length][0]);
        case_num++;
    }
    return 0;
}
