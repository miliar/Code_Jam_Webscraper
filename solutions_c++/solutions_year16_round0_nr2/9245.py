#include <cstdio>
#include <utility>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <iostream>
#include <unordered_map>
#include <stack>
#include <map>
using namespace std;

#define REP(i, x) for (int i = 0; i < (x); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define ALL(a) (a).begin(), (a).end()

typedef long long ll;

const int INF = 10000000;

int dp[1010][2];

int main() {
    int T;
    scanf("%d", &T);

    REP (i, T) {
        char S[1000];
        scanf("%s", S);

        memset(dp, 0, sizeof(dp));
        fill((int* )dp, (int* )(dp + strlen(S)), INF);

        if (S[0] == '+') {
            dp[0][0] = 0;
            dp[0][1] = 1;
        } else {
            dp[0][0] = 1;
            dp[0][1] = 0;
        }

        FOR (j, 1, strlen(S)) {
            if (S[j] == '+') {
                dp[j][0] = min(dp[j][0], dp[j - 1][0]);
                dp[j][0] = min(dp[j][0], dp[j - 1][1] + 1);
                dp[j][1] = min(dp[j][1], dp[j - 1][0] + 1);
                dp[j][1] = min(dp[j][1], dp[j - 1][1] + 2);
            } else {
                dp[j][0] = min(dp[j][0], dp[j - 1][0] + 2);
                dp[j][0] = min(dp[j][0], dp[j - 1][1] + 1);
                dp[j][1] = min(dp[j][1], dp[j - 1][0] + 1);
                dp[j][1] = min(dp[j][1], dp[j - 1][1]);
            }
        }
        
        printf("Case #%d: %d\n", i + 1, dp[strlen(S)-1][0]);
    }

    return 0;
}
