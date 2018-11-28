#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <sstream>
using namespace std;
#pragma comment(linker, "/STACK:255000000")

typedef long long ll;

#define rep(i, a, b) for(i = (a); i < (b); ++i)
#define repb(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define repd(i, a, b, d) for(i = (a); i < (b); i += (d))
#define repbd(i, a, b, d) for(i = (a) - 1; i >= (b); i -= (d))
#define reps(i, s) for(i = 0; (s)[i]; ++i)
#define repl(i, l) for(i = l.begin(); i != l.end(); ++i)

#define in(f, a) scanf("%"#f, &(a))

bool firstout = 1;

#define out(f, a) printf("%"#f, (a))
#define outf(f, a) printf((firstout) ? "%"#f : " %"#f, (a)), firstout = 0
#define nl printf("\n"), firstout = 1

#define all(x) (x).begin(),(x).end()
#define sqr(x) ((x) * (x))
#define mp make_pair

template<class T>
T &minn(T &a, T b)
{
    if(b < a) a = b;
    return a;
}

template<class T>
T &maxx(T &a, T b)
{
    if(a < b) a = b;
    return a;
}

#define inf 1012345678
#define eps 1e-9


#ifdef XDEBUG
#define mod 23
#else
#define mod 1000000007
#endif

int &madd(int &a, int b)
{
    a += b;
    if(a >= mod) a -= mod;
    return a;
}

int &msub(int &a, int b)
{
    a -= b;
    if(a < 0) a += mod;
    return a;
}

int &mmult(int &a, int b)
{
    return a = (ll)a * b % mod;
}

int mdiv(ll a, ll b, ll m)
{
    a = (a % m + m) % m;
    b = (b % m + m) % m;
    if(a % b == 0) return a / b;
    return (a + m * mdiv(-a, m, b)) / b;
}

#define N 1012
#define M 1012

int DX[4] = {-1, 0, 0, 1};
int DY[4] = {0, -1, 1, 0};

int n, m, q, x;
int A[N][N];
vector<int> V[N];

bool valid(int i, int j) {
    return 0 <= i && i < n && 0 <= j && j < m;
}

int dfs(int i, int j) {
    int res = A[i][j];
    A[i][j] = 0;
    int k;
    rep(k, 0, 4) {
        int ii = i + DX[k];
        int jj = j + DY[k];
        if (valid(ii, jj) && A[ii][jj]) res += dfs(ii, jj);
    }
    return res;
}

bool can(int pat, int _n, int _m) {
    n = _n;
    m = _m;
    int i, j, ii, jj;
    rep (i, 0, n) rep(j, 0, m) {
            rep (ii, 0, 5) {
                rep (jj, 0, 5) if (pat >> ii * 5 >> jj & 1 && !valid(i + ii, j + jj)) break;
                if (jj < 5) break;
            }
            if (ii == 5) {
                rep (ii, 0, n) rep (jj, 0, m) A[ii][jj] = 1;
                rep (ii, 0, 5) rep (jj, 0, 5) A[i + ii][j + jj] -= pat >> ii * 5 >> jj & 1;
                rep (ii, 0, n) {
                    rep (jj, 0, m) if (A[ii][jj]) {
                            int a = dfs(ii, jj);
                            if (a % x) break;
                        }
                    if (jj < m) break;
                }
                if (ii == n) return 1;
            }
        }
    return 0;
}

int main()
{
#ifdef XDEBUG
	freopen("in.txt", "rt", stdin);
#else
    freopen("x.in", "rt", stdin);
    freopen("x.out", "wt", stdout);
#endif

    int i, j, k;
    char c;
    int a, d;

    rep(i, 0, 7) V[i].clear();
    n = m = 5;
    rep(k, 0, 1 << 25) {
        rep(i, 0, 5) if (k >> i & 1) break;
        if (i == 5) continue;
        rep(i, 0, 5) if (k >> i * 5 & 1) break;
        if (i == 5) continue;
        int l = 0;
        rep(i, 0, 25) l += k >> i & 1;
        if (3 <= l && l <= 6) {
            rep(i, 0, n) rep(j, 0, m) A[i][j] = k >> i * 5 >> j & 1;
            rep(i, 0, n) {
                rep(j, 0, m) if (A[i][j]) break;
                if (j < m) break;
            }
            a = dfs(i, j);
            if (a == l) V[l].push_back(k);
        }
    }

    int ts;
#if 1
    int tss;
    in(d, tss);
    rep(ts, 1, tss + 1)
#else
    for(ts = 1; in(d, n) > 0; ++ts)
#endif
    {
        int n, m;
        in(d, x);
        in(d, n);
        in(d, m);
        printf("Case #%d: ", ts);
        if (x >= 7 || x > max(n, m) || n * m % x) out(s, "RICHARD");
        else if (x <= 2) out(s, "GABRIEL");
        else {
            rep(i, 0, V[x].size()) if(!can(V[x][i], n, m) && !can(V[x][i], m, n)) break;
            if (i < V[x].size()) out(s, "RICHARD");
            else out(s, "GABRIEL");
        }
        nl;
#ifndef XDEBUG
        cerr << ts << endl;
#endif
    }

    return 0;
}
