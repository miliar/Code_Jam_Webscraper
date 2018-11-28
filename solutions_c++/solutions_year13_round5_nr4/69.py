#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int T, n;
char s[21];
double dp[1 << 20];

int main() {
    scanf("%d", &T);
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        scanf("%s", s);
        n = strlen(s);
        int status = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] == 'X') {
                status |= 1 << i;
            }
        }
        memset(dp, 0, sizeof(dp));
        for (int i = (1 << n) - 2; i >= 0; --i) {
            if ((i & status) != status) {
                continue;
            }
            for (int j = 0; j < n; ++j) {
                double money = 0.0;
                int next = j;
                for (int k = 0; k < n && (i >> (j + k) % n & 1) == 1; ++k) {
                    ++money;
                    next = (next + 1) % n;
                }
                money = n - money;
                dp[i] += (dp[i | 1 << next] + money) / n;
            }
        }
        printf("Case #%d: %.13f\n", caseNum, dp[status]);
    }
    return 0;
}
