// ================================================================================================
//  GCJ053A.cpp
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
#include <queue>

using namespace std;

#if defined _OJ_PROJECT
_BEGIN_PROBLEM(_GCJ15_03A, "GCJ15 03A")
#endif // _OJ_PROJECT

#define infinite_loop for (;;)

char table[100][1001];

int solve(int R, int C) {
    int ans = 0;
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            if (table[i][j] != '.') {
                bool left = false, right = false, top = false, bottom = false;

                for (int k = j - 1; k >= 0; --k)
                    if (table[i][k] != '.') {
                        left = true;
                        break;
                    }

                for (int k = j + 1; k < C; ++k)
                    if (table[i][k] != '.') {
                        right = true;
                        break;
                    }

                for (int k = i - 1; k >= 0; --k)
                    if (table[k][j] != '.') {
                        top = true;
                        break;
                    }

                for (int k = i + 1; k < R; ++k)
                    if (table[k][j] != '.') {
                        bottom = true;
                        break;
                    }

                if (!top && !bottom && !left && !right)
                    return -1;

                if ((table[i][j] == '^' && !top) ||
                    (table[i][j] == 'v' && !bottom) ||
                    (table[i][j] == '<' && !left) ||
                    (table[i][j] == '>' && !right))
                    ++ans;
            }
    return ans;
}

int main() {
    int T, R, C;
    scanf("%d", &T);

    for (int _T = 1; _T <= T; ++_T) {
        scanf("%d %d", &R, &C);

        for (int i = 0; i < R; ++i) scanf("%s", table[i]);

        int ans = solve(R, C);
        if (ans == -1)
            printf("Case #%d: IMPOSSIBLE\n", _T);
        else
            printf("Case #%d: %d\n", _T, ans);
    }

    return 0;
}

#if defined _OJ_PROJECT
_END_PROBLEM
#endif // _OJ_PROJECT

// ================================================================================================
//  End of file.
// ================================================================================================
