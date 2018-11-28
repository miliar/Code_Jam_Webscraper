// Written by Luis Garcia, 2016.
// OJ-ID: CJ1603C

#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int dp[1 << 16], order[1 << 16];

inline int bits(int n) {
    int c = 0;
    for (; n != 0; n >>= 1) c += n & 1;
    return c;
}

int main() {
    char A[30];

    int topics[20][2];

    int T, N;
    scanf("%d", &T);
    for (int _T = 1; _T <= T; ++_T) {
        scanf("%d", &N);

        map<string, int> words;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < 2; ++j) {
                scanf("%s", A);
                int & p = words[A];
                if (!p) p = words.size();
                topics[i][j] = p;
            }
        }

        int M = 1 << N;
        for (int j = 0; j < M; ++j) order[j] = j;
        sort(order, order + M, [](int a, int b){ return bits(a) < bits(b); });

        memset(dp, 0, sizeof dp);
        for (int j = 0; j < M - 1; ++j) {
            int mask = order[j];
            for (int i = 0, _i = 1; i < N; ++i, _i <<= 1)
                if ((mask & _i) == 0) {
                    bool a = false, b = false;
                    for (int k = 0, _k = 1; k < N; ++k, _k <<= 1)
                        if ((mask & _k) != 0) {
                            a |= topics[i][0] == topics[k][0];
                            b |= topics[i][1] == topics[k][1];
                        }
                    dp[mask | _i] = max(dp[mask | _i], dp[mask] + (a && b ? 1 : 0));
                }
        }

        printf("Case #%d: %d\n", _T, dp[M - 1]);
    }
    return 0;
}
