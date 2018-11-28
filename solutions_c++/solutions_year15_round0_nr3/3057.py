/*
 * Author:  xioumu
 * Created Time:  2015/4/11 20:06:58
 * File Name: C.cpp
 * solve: C.cpp
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
const int maxn = 10;
const int maxm = 100000 + 10;

int sgn(const double &x) {  return (x > eps) - (x < -eps); }

int a[maxn][maxn] = {{},
                     {0, 1, 2, 3, 4},
                     {0, 2, -1, 4, -3},
                     {0, 3, -4, -1, 2},
                     {0, 4, 3, -2, -1}}; 
int n;
int b[maxn][maxn], c[maxm], sum[maxm];
char l[maxm];

void init() {
    clr(b);
    repf (i, 1, 4)
        repf (j, 1, 4) {
            int op = 1;
            int k = a[i][j];
            if (k < 0) {
                op = -op;
                k = -k;
            }
            b[k][i] = op * j;
        }
    //repf (i, 1, 4) {
        //repf (j, 1, 4) {
            //printf ("%d ", b[i][j]);
        //}
        //cout << endl;
    //}
    
}

int getVal(char c) {
    if (c == '1') return 1;
    if (c == 'i') return 2;
    if (c == 'j') return 3;
    if (c == 'k') return 4;
}

int get(int x, int y) {
    int op = 1;
    int k = sum[y];
    int k2 = sum[x - 1];
    if (k < 0) {
        op = -op;
        k = -k;
    }
    if (k2 < 0) {
        op = -op;
        k2 = -k2;
    }
    return op * b[k][k2];
}

bool check(int x, int y) {
    int v2 = get(x + 1, y);
    int v3 = get(y + 1, n - 1);
    //printf ("%d %d %d %d %d\n", x, y, sum[x], v2, v3);
    if (sum[x] != 2) return false;
    if (v2 != 3) return false;
    if (v3 != 4) return false;
    return true;
}

int main() {
    int T, ca = 1;
    init();
    freopen("C.out", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        int m, x;
        n = 0;
        scanf("%d%d", &m, &x);
        scanf("%s", l);
        rep (i, x) {
            rep (j, m) {
                c[n++] = getVal(l[j]); 
            }
        }
        sum[0] = c[0];
        repf (i, 1, n - 1) {
            int v = sum[i - 1], op = 1;
            if (v < 0) {
                v = -v;
                op = -op;
            }
            sum[i] = op * a[v][c[i]];
        }
        //rep (i, n)
            //printf("%d ", sum[i]);
        //puts("");

        bool ans = false;
        rep (i, n - 2) {
            repf (j, i + 1, n - 2) {
                if (check(i, j)) {
                    ans = true;
                    break;
                } 
            } 
            if (ans)
                break;
        }
        printf("Case #%d: ", ca++);
        if (ans) printf("YES\n");
        else printf("NO\n");
        
    }
    return 0;
}
