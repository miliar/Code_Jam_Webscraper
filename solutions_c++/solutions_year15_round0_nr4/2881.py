#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <sstream>
#include <fstream>
#define debug puts("-----")
#define ll long long int
const double pi = acos(-1.0);
const double eps = (1e-8);
const int inf = 1 << 31;
using namespace std;

int a[5][5][5];
void init()
{
    for (int i = 1; i <= 4; i++)
    {
        for (int j = 1; j <= 4; j++)
        {
            a[1][i][j] = 1;
            if ((i * j) % 2 == 0) a[2][i][j] = 1;
        }
    }
    a[3][2][3] = a[3][3][2] = a[3][3][3] = a[3][4][3] = a[3][3][4] = 1;
    a[4][3][4] = a[4][4][3] = a[4][4][4] = 1;
}

int main(int argc, char const *argv[])
{
    init();
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int T, x, r, c;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        scanf("%d%d%d", &x, &r, &c);
        printf("Case #%d: %s\n", cas, a[x][r][c] == 1 ? "GABRIEL" : "RICHARD");
    }
    return 0;
}

