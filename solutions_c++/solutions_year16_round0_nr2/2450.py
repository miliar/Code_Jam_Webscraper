#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define TASK "B-large"

const int N = 105;
const int INF = 0x3f3f3f3f;

char str[N];
int a[N];
int dp[N][2];

void work(int cas) {
    scanf("%s", str + 1);
    int n = strlen(str + 1);
    for (int i = 1; i <= n; i++) a[i] = (str[i] == '-');
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < 2; j++) {
            int &ret = dp[i][j];
            ret = INF;
            for (int k = i; k >= 1; k--) {
                if (a[i] != a[k]) break;
                if (j == a[i]) {
                    ret = min(ret, dp[k-1][j^1] + 1);
                    ret = min(ret, dp[k-1][j]);
                }else {
                    ret = min(ret, dp[k-1][j^1] + 1);
                    ret = min(ret, dp[k-1][j] + 2);
                }
            }
        }
    }
    printf("Case #%d: %d\n", cas, dp[n][0]);
    return ;
}

int main() {
    if (strlen(TASK) != 0) {
        freopen(TASK".in", "r", stdin);
        freopen(TASK".out", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        work(cas);
    }
    return 0;
}
