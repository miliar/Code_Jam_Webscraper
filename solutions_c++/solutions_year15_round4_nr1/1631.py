
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <cstdio>
#include <vector>
#include <string>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define mem(a, b) (memset(a, b, sizeof(a)))
#define pb push_back
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define rep(i, m) for (int i = 0; i < (int)(m); i++)
#define rep2(i, n, m) for (int i = n; i < (int)(m); i++)
typedef long long LL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;

const int oo = (int) 1e9;
const double eps = 1e-9;
#define debug(...) fprintf(stderr, __VA_ARGS__)

char ch[110][110];
int can[110][110];
int r, c;

bool vis[110][110];
void bfs(int sx, int sy) {
    int x = sx, y = sy;
    if (can[x][y] != -1) return ;

    //memset(vis, false, sizeof(vis));
    int dx = 0, dy = 0;
    int lstx = x, lsty = y;
    //vis[x][y] = true;
    while ( 1 ) {
        if (ch[x][y] == '>') {
            dx = 0; dy = 1;
        } else if (ch[x][y] == '<') {
            dx = 0; dy = -1;
        } else if (ch[x][y] == 'v') {
            dx = 1; dy = 0;
        } else if (ch[x][y] == '^') {
            dx = -1; dy = 0;
        }
        int xx = x + dx, yy = y + dy;
        if (xx < 0 || xx >= r || yy < 0 || yy >= c) {
            if (lstx != sx && lsty != sy)
                can[lstx][lsty] = 1;
            return ;
        }
        //if (vis[xx][yy] == true) return ;
        if (ch[xx][yy] != '.') {
            can[lstx][lsty] = 0;
            lstx = xx, lsty = yy;
         //   vis[xx][yy] = true;
        }
        if (can[xx][yy] != -1) return ;
    }
}

int main(void) {
    int T;
    int cas = 1;
    scanf("%d", &T);
    while (T -- > 0) {
        scanf("%d %d", &r, &c);
        for (int i = 0; i < r; ++ i) {
            getchar();
            for (int j = 0; j < c; ++ j) {
                scanf("%c", &ch[i][j]);
            }
        }

        memset(can, -1, sizeof(can));

        for (int i = 0; i < r; ++ i) if (ch[i][0] == '<') can[i][0] = 1;
        for (int i = 0; i < r; ++ i) if (ch[i][c-1] == '>') can[i][c-1] = 1;
        for (int i = 0; i < c; ++ i) if (ch[0][i] == '^') can[0][i] = 1;
        for (int i = 0; i < c; ++ i) if (ch[r-1][i] == 'v') can[r-1][i] = 1;
        for (int i = 0; i < r; ++ i) for (int j = 0; j < c; ++ j) if (ch[i][j] != '.') {
            bfs(i, j);
        }

        bool flag = true;
        int result = 0;
        for (int i = 0; i < r; ++ i) for (int j = 0; j < c; ++ j) if (ch[i][j] != '.') {
            if (can[i][j] == -1) {
                flag = false;
                break;
            } else if (can[i][j] == 1) {
                ++ result;
            }
        }
        printf("Case #%d: ", cas ++);
        if (flag == false) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", result);
        }
    }

    return 0;
}
