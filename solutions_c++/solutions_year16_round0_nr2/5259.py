#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

#define eps 0.0000001
#define pi  3.14159265359
#define inf 2000000000

typedef long long lld;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

const int MAXN = 100 + 5;

int n, dp[MAXN][2];
char S[MAXN];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int tt;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        scanf("%s", S);
        n = strlen(S);
        if (S[0] == '-') {
            dp[0][0] = 0;
            dp[0][1] = 1;
        } else {
            dp[0][0] = 1;
            dp[0][1] = 0;
        }
        for (int i = 1; i < n; i++) {
            if (S[i] == '-') {
                dp[i][0] = min(dp[i - 1][0], dp[i - 1][1] + 2);
                dp[i][1] = dp[i - 1][0] + 1;
            } else {
                dp[i][0] = dp[i - 1][1] + 1;
                dp[i][1] = min(dp[i - 1][1], dp[i - 1][0] + 2);
            }
        }
        printf("Case #%d: %d\n", t, dp[n - 1][1]);
    }
    return 0;
}
