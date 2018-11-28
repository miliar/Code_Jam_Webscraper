#include <bits/stdc++.h>

#define all(v) (v).begin(), (v).end()

typedef long long ll;
typedef unsigned long long ull;

const int INF = 1e8;

using namespace std;

bool d[100000];
// dp[i][j] := i:index j:if all '+' then 1 else all '-' then 0
long long dp[100000][2];

int main() {
    int T;
    string S;
    while(cin >> T) {
        for(int t = 1; t <= T; t++) {
            cin >> S;
            memset(d, 0, sizeof d); 
            int N = S.size();
            for(int i = 0; i < N; i++) {
                for(int j = 0; j < 2; j++) {
                    dp[i][j] = INF;
                }
            }

            for(int i = 0; i < N; i++) {
                if(S[i] == '-') d[i] = 0;
                else d[i] = 1;
            }

            if(d[0]) {
                dp[0][0] = 1;
                dp[0][1] = 0;
            } else {
                dp[0][0] = 0;
                dp[0][1] = 1;
            }

            for(int i = 1; i < N; i++) {
                if(d[i]) { // '+'
                    // flip
                    dp[i][0] = min(dp[i][0], dp[i-1][1] + 1LL);
                    // not change
                    dp[i][1] = min(dp[i][1], dp[i-1][1]);
                } else { // '-'
                    // flip
                    dp[i][1] = min(dp[i][1], dp[i-1][0] + 1LL);
                    // not change
                    dp[i][0] = min(dp[i][0], dp[i-1][0]);
                }
            }

            printf("Case #%d: %lld\n", t, dp[N-1][1]);
        }
    }
}

