#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <fstream>
#include <cstring>

using namespace std;

char s[200];

int main() {
    int T, n;
    freopen("B-large.in","r",stdin);
    freopen("Blarge.out","w",stdout);
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);

        scanf("%s", s);

        n = strlen(s);

        vector< vector<int> > dp(2);
        dp[0].resize(n + 1, 0);
        dp[1].resize(n + 1, 0);

        dp[0][0] = dp[1][0] = 0;
        for (int i = 0; i < n; i++) {

            if (i && s[i - 1] == s[i]) {
                dp[0][i + 1] = min(dp[0][i], dp[1][i] + 1);
                dp[1][i + 1] = min(dp[1][i], dp[0][i] + 1);
            } else if (s[i] == '+') {
                dp[0][i + 1] = min(dp[0][i], dp[1][i] + 1);
                dp[1][i + 1] = dp[0][i] + 1;
            } else if (s[i] == '-') {
                dp[1][i + 1] = min(dp[1][i], dp[0][i] + 1);
                dp[0][i + 1] = dp[1][i] + 1;
            }
        }

        printf("%d\n", min(dp[0][n], dp[1][n] +1));
    }



    return 0;
}
