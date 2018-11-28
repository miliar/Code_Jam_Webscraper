/*
 * Author:  xioumu
 * Created Time:  2013/4/13 18:24:55
 * File Name: b.cpp
 * solve: b.cpp
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

int n, m, a[maxn][maxn];
int row[maxn], line[maxn];
vector<int> x[maxn], y[maxn];

int main() {
    int T, ca = 1, can[maxn][maxn];
    freopen("b.out", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        memset(can, 0, sizeof(can));
        scanf("%d%d", &n, &m);
        rep (i, n)
            rep (j, m)
                scanf("%d", &a[i][j]);
        rep (i, maxn)
            x[i].clear(), y[i].clear();
        rep (i, n) {
            row[i] = 0;
            rep (j, m) {
                row[i] = max(row[i], a[i][j]);
                x[a[i][j]].push_back(i);
                y[a[i][j]].push_back(j);
            }
        }
        rep (i, m) {
            line[i] = 0;
            rep (j, n)
                line[i] = max(line[i], a[j][i]);
        }
        
        repd (i, 100, 1) {
            rep (j, sz(x[i])) {
                if (row[x[i][j]] == i) can[x[i][j]][y[i][j]] = 1;
                if (line[y[i][j]] == i) can[x[i][j]][y[i][j]] = 1;
            }
        }
        
        //rep (i, n) {
            //rep (j, m) {
                //printf("%d ", can[i][j]);
            //}
            //puts("");
        //}
        int ans = 1;
        rep (i, n)
            rep (j, m) {
                if (can[i][j] == 0)
                    ans = 0;
            }
        printf("Case #%d: ", ca++);
        if (ans == 0) printf("NO\n");
        else printf("YES\n");
    }
    return 0;
}
