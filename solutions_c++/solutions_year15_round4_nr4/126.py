//Coder: Balajiganapathi
#ifndef ONLINE_JUDGE
#   define DEBUG
#   define TRACE
#else
//#   define NDEBUG
#endif

#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
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
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;
typedef vector<pi> vpi;

// Basic macros
#define fi          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define rep(i,s,n)  for(int i=s;i<=(n);++i)
#define fo(i,n)     re(i,0,n)
#define rev(i,n,s)  for(int i=(n)-1;i>=s;--i)
#define repv(i,n,s) for(int i=(n);i>=s;--i)
#define fov(i,n)    rev(i,n,0)
#define pu          push_back
#define mp          make_pair
#define si(x)       (int)(x.size())

#ifdef TRACE
    #define trace(x)            cerr<<x<<endl;
    #define trace1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
    #define trace4(a,b,c,d)     cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<endl;
    #define trace5(a,b,c,d,e)   cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<endl;
    #define trace6(a,b,c,d,e,f) cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<" | "#f" = "<<f<<endl;
#else
    #define trace(x)
    #define trace1(x)
    #define trace2(x,y)
    #define trace3(x,y,z)
    #define trace4(a,b,c,d)
    #define trace5(a,b,c,d,e)
    #define trace6(a,b,c,d,e,f)
#endif

const int oo = 1000000009;
const double eps = 1e-6;
const int mod = 1000000007;
const int mx = 6;

int n, m;
int num[mx][mx];

int ans;
int di[] = {-1, 1, 0, 0}, dj[] = {0, 0, -1, 1};
#define set(mask, n) ((mask >> n) & 1)

bool is_eq(vector<vi> a, vector<vi> b) {
    fo(fj, m) {
        bool ok = true;
        fo(i, n) {
            fo(j, m) {
                if(a[i][(fj + j) % m] != b[i][j]) {
                    ok = false;
                    break;
                }
            }
            if(!ok) break;
        }
        if(ok) return true;
    }
    return false;
}

vector<vector<vi> >  sols;
bool valid(int i, int j) {
    return i >= 0 && i < n && j >= 0 && j < m;
}
bool ispos(int i, int j, int c, int rec) {
    //assert(valid(i, j) && c != -1 && c >= 1 && c <= 3);
    int empty_cells = 0, eq_c = 0;
    fo(d, 4) {
        int ni = i + di[d], nj = j + dj[d];
        if(nj == -1) nj = m - 1;
        if(nj == m) nj = 0;
        if(!valid(ni, nj)) continue;
        if(num[ni][nj] == -1) ++empty_cells;
        if(num[ni][nj] == c) ++eq_c;
    }
    //trace6(i, j, num[i][j], c, eq_c, empty_cells);
    //if(num[i][j] == c) return eq_c == c;
    if(eq_c > c || empty_cells < c - eq_c) return false;

    if(rec == 0) return true;

    bool just = false;
    if(num[i][j] == -1) {
        just = true;
        num[i][j] = c;
    }

    bool ok = true;
    fo(d, 4) {
        int ni = i + di[d], nj = j + dj[d];
        if(nj == -1) nj = m - 1;
        if(nj == m) nj = 0;
        if(valid(ni, nj) && num[ni][nj] != -1 && !ispos(ni, nj, num[ni][nj], 0)) {
            ok = false;
            break;
        }
    }
    if(just) {
        num[i][j] = -1;
    }
    return ok;
}

void rec(int i, int j) {
    if(j == m) {
        rec(i + 1, 0);
        return;
    }
    if(i == n) {
        fo(ii, n) fo(jj, m) if(!ispos(ii, jj, num[ii][jj], 0)) return;
        vector<vi> cur(n, vi(m));
        fo(ii, n) fo(jj, m) {
            cur[ii][jj] = num[ii][jj];
        }
        fo(k, si(sols)) if(is_eq(cur, sols[k])) return;
        sols.pu(cur);
        ++ans;
        /*
        fo(ii, n) {
            fo(jj, m) printf("%d ", num[ii][jj]);
            printf("\n");
        }
        printf("\n");
        */
        return;
    }
    //trace2(i, j);
    //assert(valid(i, j));

    rep(nxt, 1, 3) {
        if(ispos(i, j, nxt, 1)) {
            num[i][j] = nxt;
            rec(i, j + 1);
            num[i][j] = -1;
        }
    }
}

int main() {
    //freopen("sample.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    freopen("D-small-attempt0.in", "r", stdin);
    freopen("small0.txt", "w", stdout);

    //freopen("D-large.in", "r", stdin);
    //freopen("large.txt", "w", stdout);
    
    int kases;
    scanf("%d", &kases);
    for(int kase = 1; kase <= kases; ++kase) {
        scanf("%d %d", &n, &m);
        ans = 0;
        ini(num, -1);
        sols.clear();
        rec(0, 0);

        trace2(kase, ans);
        printf("Case #%d: %d\n", kase, ans);
    }
    
	return 0;
}
