#include <iostream>
#include <sstream>
#include <vector>
#include <windows.h>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <map>
#include <set>
#include <cmath>

using namespace std;

#define pb push_back
#define mp make_pair
#define INF 1000000000
#define y1 tratatatatatatata

const int MOD = 1000000007;

int allC = 0;
bool finished;
int b[55][55], a[55][55];
bool used[55][55];
int canG[55][559];
int n, m, c;

inline bool goodX(int x, int y) {
    return (x >= 0 && x < n && y >= 0 && y < m);
}

void print() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j)
            if (b[i][j] == 0) printf(".");
            else if (b[i][j] == 1) printf("*");
            else if (b[i][j] == 2) printf(".");
            else printf("c");
        printf("\n");
    }
}

void dfs(int x, int y) {
    used[x][y] = true;
    for (int dx = -1; dx <= 1; ++dx)
        for (int dy = -1; dy <= 1; ++dy) {
            if (!goodX(x+dx,y+dy)) continue;
            int xx = x + dx, yy = y + dy;
            if (used[xx][yy] || b[xx][yy] != 0) continue;
            dfs(xx, yy);
        }
}

bool check() {
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            if (b[i][j] == 2) {
                bool ok = false;
                for (int dx = -1; dx <= 1; ++dx)
                    for (int dy = -1; dy <= 1; ++dy)
                        if (goodX(i + dx, j + dy) && b[i + dx][j + dy] == 0) ok = true;
                if (!ok) return false;
            }
        }
    memset(used, false, sizeof(used));
    bool ok = false;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (!used[i][j] && b[i][j] == 0) {
                if (ok) return false;
                dfs(i, j);
                ok = true;
            }
    return true;
}

int tmp;

void rec(int x, int y) {

    if (finished) return;

    if (allC + canG[x][y] < c) return;

    if (x == n) {
        if (allC != c) return ;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (a[i][j] == 0) {
                    b[i][j] = 0;
                    for (int dx = -1; dx <= 1; ++dx)
                        for (int dy = -1; dy <= 1; ++dy)
                            if (goodX(i+dx, j+dy) && a[i+dx][j+dy] == 1) b[i][j] = 2;
                }
                else b[i][j] = a[i][j];

        if (check()) {
            bool found = false;
            finished = true;
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < m; ++j)
                    if (!found && b[i][j] != 1) {
                        if (b[i][j] == 0) {
                            found = true;
                            b[i][j] = 3;
                        }
                    }
            if (!found) {
                for (int i = 0; i < n; ++i)
                    for (int j = 0; j < m; ++j)
                        if (!found && b[i][j] != 1) {
                            found = true;
                            b[i][j] = 3;
                        }
            }
            print();
        }
        return;
    }

    int xx = x, yy = y + 1;
    if (yy >= m) yy = 0, xx += 1;
    a[x][y] = 0;
    rec(xx, yy);
    allC++;
    a[x][y] = 1;
    rec(xx, yy);
    allC--;
    a[x][y] = 0;
}

void solve(){
    scanf("%d%d%d",&n,&m,&c);
    if (n * m == c) {
        printf("Impossible\n");
        return;
    }
    if (n * m == c + 1) {
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                b[i][j] = 1;
        b[0][0] = 3;
        print();
        return;
    }
    finished = false;
    allC = 0;
    tmp = 0;

    int q = 1;
    for (int i = n - 1; i >= 0; --i)
        for (int j = m - 1; j >= 0; --j)
            canG[i][j] = q++;

    rec(0, 0);
    if (!finished) printf("Impossible\n");
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    scanf("%d",&t);
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d:\n", i);
        solve();
    }
    return 0;
}
