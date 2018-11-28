#pragma comment(linker, "/STACK:6400000000000")

#define _USE_MATH_DEFINES

#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
#include <iomanip>
#include <ctime>
#include <stack>
#include <bitset>
using namespace std;

typedef long long ll;
typedef long double ld;

const ld EPS = 1e-12;
const int INF = (int)(2e9 + 0.5);
const int MAXN = 10005;

int t, x, r, c, dp[10][10][10];

void init() {
    for(int k = 1; k <= 4; ++k) {
        for(int i = 1; i <= 4; ++i) {
            for(int j = 1; j <= 4; ++j) {
                dp[k][i][j] = 2;
            }
        }
    }

    dp[2][1][1] = 1;
    dp[2][1][3] = 1;
    dp[2][3][1] = 1;
    dp[2][3][3] = 1;

    dp[3][1][1] = 1;
    dp[3][1][2] = 1;
    dp[3][1][3] = 1;
    dp[3][1][4] = 1;
    dp[3][2][1] = 1;
    dp[3][2][2] = 1;
    dp[3][2][4] = 1;
    dp[3][3][1] = 1;
    dp[3][4][1] = 1;
    dp[3][4][2] = 1;
    dp[3][4][4] = 1;

    dp[4][1][1] = 1;
    dp[4][1][2] = 1;
    dp[4][1][3] = 1;
    dp[4][1][4] = 1;
    dp[4][2][1] = 1;
    dp[4][2][2] = 1;
    dp[4][2][3] = 1;
    dp[4][2][4] = 1;
    dp[4][3][1] = 1;
    dp[4][3][2] = 1;
    dp[4][3][3] = 1;
    dp[4][3][4] = 2;
    dp[4][4][1] = 1;
    dp[4][4][2] = 1;
    dp[4][4][3] = 2;
    dp[4][4][4] = 2;
}

int main() {
    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);
    init();
    scanf("%d", &t);
    for(int q = 1; q <= t; ++q) {
        scanf("%d%d%d", &x, &r, &c);
        printf("Case #%d: ", q);
        printf(dp[x][r][c] == 1 ? "RICHARD\n" : "GABRIEL\n");
    }
    return 0;
}
