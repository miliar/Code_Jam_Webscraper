// ================================================================================================
//  A - Standing Ovation.cpp
//  Written by Luis Garcia, 2015
// ================================================================================================

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <iterator>
#include <numeric>
#include <iostream>

using namespace std;

#if defined _OJ_PROJECT
_BEGIN_PROBLEM(_GCJ15_01C, "GCJ15 01C")
#endif // _OJ_PROJECT

#define infinite_loop for (;;)

int main() {
    bool fromLeft[2][8][10100];
    int fromRight[10100];
    char S[10100], SC[10100];

    auto sgn = [](int t) { return (0 < t) - (t < 0); };
    auto toId = [](int t) { return t < 0 ? abs(t) + 3 : t - 1; };

    int table[4][4] = {
        {1,  2,  3,  4},
        {2, -1,  4, -3},
        {3, -4, -1,  2},
        {4,  3, -2, -1},
    };

    int extendedTable[8][8] = {};

    for (int i = -4; i <= 4; ++i)
        for (int j = -4; j <= 4; ++j) {
            if (!i || !j) continue;
            int r = table[abs(i) - 1][abs(j) - 1] * sgn(i) * sgn(j);
            extendedTable[toId(i)][toId(j)] = toId(r);
        }

    int T, L, X;
    scanf("%d", &T);
    for (int _T = 1; _T <= T; ++_T) {
        scanf("%d %d %s", &L, &X, S);

        strcpy(SC, S);
        for (int i = 1; i < X; ++i) strcat(SC, S);

        int N = L * X;

        fromLeft[0][0][0] = 0;
        fromRight[N] = 0;

        for (int i = N - 1; i >= 0; --i)
            fromRight[i] = extendedTable[S[i % L] - 'i' + 1][fromRight[i + 1]];

        memset(fromLeft, 0, sizeof fromLeft);
        fromLeft[0][0][0] = true;
        for (int i = 1; i <= N; ++i)
            for (int j = 0; j < 8; ++j) {
                int next = extendedTable[j][S[(i - 1) % L] - 'i' + 1];
                fromLeft[1][next][i] |= fromLeft[1][j][i - 1];
                fromLeft[0][next][i] |= fromLeft[0][j][i - 1];
                if (next == 1 && fromLeft[0][j][i - 1])
                    fromLeft[1][0][i] = true;
            }

        bool answer = false;
        for (int i = 1; i <= N; ++i)
            answer |= fromLeft[1][2][i] && fromRight[i] == 3;

        printf("Case #%d: %s\n", _T, answer ? "YES" : "NO");
    }

    return 0;
}

#if defined _OJ_PROJECT
_END_PROBLEM
#endif // _OJ_PROJECT

// ================================================================================================
//  End of file.
// ================================================================================================
