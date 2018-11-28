/**
 * Jerry Ma
 * A.cpp
 */

#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <bitset>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long int lli;
typedef pair<int, int> pii;

int gInt () {
    int i;
    scanf("%d", &i);
    return i;
}

lli gLong () {
    lli i;
    scanf("%lld", &i);
    return i;
}

double gDouble () {
    double i;
    scanf("%lf", &i);
    return i;
}

void quit () {
    fflush(stdout);
    exit(0);
}

int init;
int n;
int others[105];
int dp[105][1000002];

#define INF 100000

inline void setstate (int i, int j, int state) {
    dp[i][j] = min(dp[i][min(j, 1000001)], state);
}

void solve (int nC) {
    printf("Case #%d: ", nC);
    init = gInt();
    n = gInt();
    for (int i = 0; i <= n; i ++)
        for (int j = 0; j <= 1000001; j ++)
            dp[i][j] = INF;
    for (int i = 0; i < n; i ++) {
        others[i] = gInt();
    }
    sort(others, others + n);
    dp[0][init] = 0;
    for (int i = 0; i < n; i ++) {
        int curmole = others[i];
        for (int j = 0; j <= 1000001; j ++) {
            if (j > curmole) {
                setstate(i + 1, j + curmole, dp[i][j]);
            }
            else {
                setstate(i + 1, j, dp[i][j] + 1);
                if (j > 1) {
                    int newmole = j;
                    int iters = 0;
                    for (; newmole <= 1000001; iters ++) {
                        if (newmole > curmole)
                            setstate(i + 1, newmole + curmole, dp[i][j] + iters);
                        newmole = newmole * 2 - 1;
                    }
                }
            }
        }
    }
    int best = INF;
    for (int i = 0; i <= 1000001; i ++)
        best = min(best, dp[n][i]);
    printf("%d\n", best);
}

int main (int argc, char ** argv) {
    int nC = gInt();
    for (int i = 1; i <= nC; i ++)
        solve(i);
    quit();
}