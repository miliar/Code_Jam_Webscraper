#define _USE_MATH_DEFINES

#ifdef ONLINE_JUDGE
#define FINPUT(file) 0
#define FOUTPUT(file) 0
#else
#define FINPUT(file) freopen(file,"r",stdin)
#define FOUTPUT(file) freopen(file,"w",stdout)
#endif

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <set>
#include <stack>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <functional>
#include <bitset>

typedef long long ll;
typedef long double ld;
static const int N = 10;
static const int M = 19;
static const int LEN = 210;
static const int MAX = 0x7fffffff;
static const int GMAX = 0x3f3f3f3f;
static const ll LGMAX = 0x3f3f3f3f3f3f3f3f;
static const int MIN = ~MAX;
static const double EPS = 1e-9;
static const ll BASE = 1000000007;
static const int CH = 27;

int result[N][N][N];

void init()
{
    for (int i = 1; i <= 4; ++i) {
        for (int j = 1; j <= 4; ++j) {
            result[1][i][j] = 1;
        }
    }
    result[2][1][1] = 0;
    result[2][1][2] = 1;
    result[2][1][3] = 0;
    result[2][1][4] = 1;
    result[2][2][1] = 1;
    result[2][2][2] = 1;
    result[2][2][3] = 1;
    result[2][2][4] = 1;
    result[2][3][1] = 0;
    result[2][3][2] = 1;
    result[2][3][3] = 0;
    result[2][3][4] = 1;
    result[2][4][1] = 1;
    result[2][4][2] = 1;
    result[2][4][3] = 1;
    result[2][4][4] = 1;
    result[3][1][1] = 0;
    result[3][1][2] = 0;
    result[3][1][3] = 0;
    result[3][1][4] = 0;
    result[3][2][1] = 0;
    result[3][2][2] = 0;
    result[3][2][3] = 1;
    result[3][2][4] = 0;
    result[3][3][1] = 0;
    result[3][3][2] = 1;
    result[3][3][3] = 1;
    result[3][3][4] = 1;
    result[3][4][1] = 0;
    result[3][4][2] = 0;
    result[3][4][3] = 1;
    result[3][4][4] = 0;
    result[4][1][1] = 0;
    result[4][1][2] = 0;
    result[4][1][3] = 0;
    result[4][1][4] = 0;
    result[4][2][1] = 0;
    result[4][2][2] = 0;
    result[4][2][3] = 0;
    result[4][2][4] = 0;
    result[4][3][1] = 0;
    result[4][3][2] = 0;
    result[4][3][3] = 0;
    result[4][3][4] = 1;
    result[4][4][1] = 0;
    result[4][4][2] = 0;
    result[4][4][3] = 1;
    result[4][4][4] = 1;
}
int main()
{
    FINPUT("in.txt");
    FOUTPUT("out.txt");

    init();
    int t;
    while (scanf("%d", &t) != EOF) {
        for (int i = 0; i < t; ++i) {
            int x, r, c;
            scanf("%d %d %d", &x, &r, &c);
            printf("Case #%d: %s\n", i + 1, result[x][r][c] == 1? "GABRIEL" : "RICHARD");
        }
    }

    return 0;
}
