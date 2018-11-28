/*
 * Author:  xioumu
 * Created Time:  2014/5/31 22:33:48
 * File Name: B.cpp
 * solve: B.cpp
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

const int maxint = -1u>>2;
const double eps = 1e-8;
const int maxn = 1000 + 10;

int sgn(const double &x) {  return (x > eps) - (x < -eps); }

int n;
int ll[maxn], rr[maxn];
int a[maxn], c[maxn];
int f[maxn][maxn][3];

void updata(int &x, int y) {
    x = min(x, y);
}

bool cmp(const int &x, const int &y) {
    return a[x] < a[y];
}

void init() {
    repf (i, 1, n) {
        scanf("%d", &a[i]);
        c[i] = i; 
    }
    sort(c + 1, c + n + 1, cmp);
    repf (i, 1, n) {
        ll[i] = rr[i] = 0;
        repf (j, 1, c[i] - 1) {
            if (a[j] > a[c[i]]) ll[i]++; 
        }
        repf (j, c[i] + 1, n)
            if (a[j] > a[c[i]]) rr[i]++;
    }
}

int main() {
    int T, ca = 1;    
    freopen("b.out", "w", stdout);
    scanf("%d", &T);
    repf (ca, 1, T) {
        scanf("%d", &n);
        init();
        repf (i, 0, n) repf (j, 0, n) rep (k, 2)
            f[i][j][k] = maxint;
        f[1][0][0] = ll[1];
        f[1][0][1] = rr[1];
        repf (i, 1, n - 1) {
            repf (j, 0, i - 1) {
                updata(f[i + 1][j][0], f[i][j][0] + ll[i + 1]);
                updata(f[i + 1][i][1], f[i][j][0] + rr[i + 1]);
                updata(f[i + 1][j][1], f[i][j][1] + rr[i + 1]);
                updata(f[i + 1][i][0], f[i][j][1] + ll[i + 1]);
            }
        }
        int ans = maxint;
        repf (j, 0, n - 1) {
            updata(ans, f[n][j][0]); 
            updata(ans, f[n][j][1]);
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
