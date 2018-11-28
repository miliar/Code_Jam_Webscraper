#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const int MAXN = 510;

const int dx[] = { 0, 1, 0,-1};
const int dy[] = { 1, 0,-1, 0};

int w, h;
int b;

bool a[MAXN][MAXN];

int ans;

bool on_field(int x, int y) {
    return x >= 0 && x < w && y >= 0 && y < h;
}

bool dfs(int x, int y, int dir) {
    a[x][y] = 1;
    if (y == h - 1)
        return 1;
    int to = (dir + 3) % 4;
    forn(q, 4) {
        int x1 = x + dx[(to + q) % 4];
        int y1 = y + dy[(to + q) % 4];
        if (on_field(x1, y1) && !a[x1][y1]) {
            if (dfs(x1, y1, to + q))
                return 1;
        }
    }
    return 0;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d ", &T);
    forn(test, T) {
        cerr << test << '\n';
        printf("Case #%d: ", test + 1);

        scanf("%d%d%d", &w, &h, &b);
        memset(a, 0, sizeof(a));
        forn(i, b) {
            int x0, y0, x1, y1;
            scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
            forab(x, x0, x1 + 1)
                forab(y, y0, y1 + 1)
                    a[x][y] = 1;
        }

        /*forba(j, h, 0) {
            forn(i, w)
                cerr << int(a[i][j]);
            cerr << '\n';
        }
        cerr << '\n';*/

        ans = 0;

        forn(i, w)
            if (!a[i][0]) {
                if (dfs(i, 0, 0)) {
                    ans++;
                }
            }



        printf("%d\n", ans);
    }
    return 0;
}
