#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// Data Packing
int dp[10002][10002];

int main()
{
    string line;

    int cases;
    cin >> cases;

    for (int caseno = 1; caseno <= cases; caseno++) {
        int N, X;
        cin >> N >> X;
        vector <int> S(N);
        for (int i = 0; i < N; i++) {
            cin >> S[i];
        }
        sort(S.begin(), S.end());

        memset(dp, 0, sizeof(dp));
        for (int f = N - 1; f >= 0; f--) {
            for (int b = f + 1; b <= N; b++) {
                dp[f][b] = 1 + min(dp[f][b - 1], dp[f + 1][b]);
                if (S[f] + S[b - 1] <= X) {
                    dp[f][b] = min(dp[f][b], 1 + dp[f + 1][b - 1]);
                }
            }
        }
        cout << "Case #" << caseno << ": " << dp[0][N] << endl;;
    }

    return 0;
}
