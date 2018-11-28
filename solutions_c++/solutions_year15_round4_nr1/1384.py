/*
 * Author:  xioumu
 * Created Time:  2015/5/30 22:19:01
 * File Name: A.cpp
 * solve: A.cpp
 */
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<iostream>
#include<vector>
#include<queue>

using namespace std;
#define sz(v) ((int)(v).size())
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repf(i, a, b) for (int i = (a); i <= (b); ++i)
#define repd(i, a, b) for (int i = (a); i >= (b); --i)
#define clr(x) memset(x,0,sizeof(x))
#define clrs( x , y ) memset(x,y,sizeof(x))
#define out(x) printf(#x" %d\n", x)
#define sqr(x) ((x) * (x))
typedef long long lint;

const int maxint = -1u>>1;
const double eps = 1e-8;
const int maxn = 100 + 10;

int sgn(const double &x) {  return (x > eps) - (x < -eps); }

int n, m;
char a[maxn][maxn];
int b[maxn][maxn];

int bx[] = {-1, 0, 1, 0};
int by[] = {0, 1, 0, -1};

int getDir(int i, int j) {
    int dir = -1;
    if (a[i][j] == '^') dir = 0;
    else if (a[i][j] == '>') dir = 1;
    else if (a[i][j] == 'v') dir = 2;
    else if (a[i][j] == '<') dir = 3;
    return dir;
}

int ok(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

int check() {
    clr(b);
    rep (i, n) rep (j, m)  {
        if(getDir(i, j) != -1) {
            rep (k, 4) { 
                int xx = i + bx[k], yy = j + by[k];
                while (ok(xx, yy)) {
                    b[xx][yy] = 1;
                    xx += bx[k];
                    yy += by[k];
                }
            }
        }
    } 
    rep (i, n) rep(j, m) {
        if (getDir(i, j) != -1 && b[i][j] == 0)
            return false;
    }
    return true;
}

int main() {
    int T, ca = 1;
    freopen("A.out", "w", stdout);
    scanf("%d", &T);
    while(T--) {
        scanf("%d%d", &n, &m);
        rep (i, n)
            scanf("%s", a[i]);
        int ans = 0;
        int ans2 = check();
        rep (i, n) rep (j, m) {
            int dir = getDir(i, j);
            if (dir != -1) {
                int xx = i + bx[dir], yy = j + by[dir];
                int flag = 1;
                while (ok(xx, yy)) {
                    if (getDir(xx, yy) != -1) {
                        flag = 0;
                        break;
                    }
                    xx += bx[dir];
                    yy += by[dir];
                }
                if (flag) 
                    ans++;
            }
        }
        printf("Case #%d: ", ca++);
        if (ans2 == false) {
            printf("IMPOSSIBLE\n");
        }
        else printf("%d\n", ans);
    }
    return 0;
}
