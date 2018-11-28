/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<double> VD;
typedef vector<string> VS;

int t, n, m;

char cell[128][128];

const int step[][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

int get_direction(char c) {
    if (c == '^') return 0;
    if (c == '>') return 1;
    if (c == 'v') return 2;
    if (c == '<') return 3;
    while (1);
}

int check(int x, int y) {
    if (cell[x][y] == '.')
        return 0;
    int d = get_direction(cell[x][y]);
    for (int i = 0; i < 4; ++i) {
        int dir = (d + i) % 4;
        int nx = x + step[dir][0], ny = y + step[dir][1];
        bool f = false;
        while (nx >= 0 && nx < n && ny >= 0 && ny < m) {
            if (cell[nx][ny] != '.') {
                f = true;
                break;
            }
            nx += step[dir][0];
            ny += step[dir][1];
        }
        if (f) {
            if (i == 0) return 0;
            else return 1;
        }
    }
    return -1;
}

int get_res() {
    int res = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int tmp = check(i, j);
            if (tmp == -1) return -1;
            res += tmp;
        }
    }
    return res;
}

void solve() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i) {
        scanf("%s", cell[i]);
    }
    int res = get_res();
    printf("Case #%d: ", ++t);
    if (res == -1) {
        puts("IMPOSSIBLE");
    } else {
        printf("%d\n", res);
    }
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
