//#pragma comment(linker,"/STACK:100000000000,100000000000")

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <map>
#include <fstream>
#include <stack>
#include <set>
#include <iomanip>
#include <queue>
#include <map>
#include <functional>
#include <list>
#include <sstream>
#include <ctime>
#include <climits>
#include <bitset>
#include <list>
#include <cassert>
#include <complex>

using namespace std;

/* Constants begin */
const long long inf = 2e18 + 7;
const long long mod = 1e9 + 7;
const double eps = 1e-12;
const double PI = 2*acos(0.0);
const double E = 2.71828;
/* Constants end */

/* Defines begin */
#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define double long double
#define F first
#define S second
#define all(a) (a).begin(),(a).end()
#define forn(i,n) for (int (i)=0; (i)<(n); ++(i))
#define random (rand()<<16|rand())
#define sqr(x) (x)*(x)
#define base complex<double>
#define sz(a) (int)(a).size()
/* Defines end */

int n, m;
char s[105][105];
map<char, int> fx, fy;

void Solve() {
    fx['>'] = 0; fy['>'] = 1;
    fx['<'] = 0; fy['<'] = -1;
    fx['^'] = -1; fy['^'] = 0;
    fx['v'] = 1; fy['v'] = 0;
    scanf("%d %d", &n, &m);
    memset(s, 0, sizeof s);
    for (int i = 1; i <= n; ++i) {
        scanf(" %s", s[i] + 1);
    }
    bool no = false;
    int res = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (fx.count(s[i][j])) {
                int dx = fx[s[i][j]];
                int dy = fy[s[i][j]];
                int nx = i + dx, ny = j + dy;
                bool arrow = false;
                while (s[nx][ny]) {
                    if (fx.count(s[nx][ny])) {
                        arrow = true;
                        break;
                    }
                    nx += dx;
                    ny += dy;
                }
                if (!arrow) {
                    bool good = false;
                    for (int dx = -1; dx <= 1; ++dx) {
                        for (int dy = -1; dy <= 1; ++dy) {
                            if (abs(dx) + abs(dy) != 1) continue;
                            int nx = i + dx, ny = j + dy;
                            bool arrow = false;
                            while (s[nx][ny]) {
                                if (fx.count(s[nx][ny])) {
                                    arrow = true;
                                    break;
                                }
                                nx += dx;
                                ny += dy;
                            }
                            good |= arrow;
                        }
                    }
                    if (!good) {
                        no = true;
                    }
                    ++res;
                }
            }
        }
    }
    if (no) {
        printf("IMPOSSIBLE\n");
    } else {
        printf("%d\n", res);
    }
}

int main(void) {
    #ifdef nobik
        freopen("input.txt", "rt", stdin);
        freopen("output.txt", "wt", stdout);
    #endif
    int t; scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        Solve();
    }
    return 0;
}
