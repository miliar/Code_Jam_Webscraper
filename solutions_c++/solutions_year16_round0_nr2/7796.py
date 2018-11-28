#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

char str[105];
int dp[2][105];

int main() {
    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; ++test) {
        scanf("%s", str);
        fill(dp[0], dp[0]+101, 0);
        fill(dp[1], dp[1]+101, 0);
        int n = strlen(str);

        for(int i = 0; i < n; ++i) {
            if(str[i] == '+') {
                dp[0][i+1] = dp[0][i];
                dp[1][i+1] = dp[0][i] + 1;
            } else {
                dp[0][i+1] = dp[1][i] + 1;
                dp[1][i+1] = dp[1][i];
            }
        }

        printf("Case #%d: %d\n", test, dp[0][n]);
    }

    return 0;
}
