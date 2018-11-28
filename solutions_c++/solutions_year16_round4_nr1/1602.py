#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:128777216")

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <sstream>

#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>

#include <math.h>
#include <cmath>
#include <string>
#include <cstring>
#include <string.h>

#include <memory.h>
#include <cassert>
#include <time.h>

using namespace std;

#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i,a,b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, b, a) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)

#define _(a, val) memset (a, val, sizeof (a))
#define sz(a) (int)((a).size())
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()

typedef long long lint;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vii;

const lint LINF = 1000000000000000000LL;
const int INF = 1000000000;
const long double eps = 1e-9;
const long double PI = 3.1415926535897932384626433832795l;

#ifdef MY_DEBUG
#define dbgx( x ) { cerr << #x << " = " << x << endl; }
#define dbg( ... ) { fprintf(stderr, __VA_ARGS__); fflush(stderr); }
#else
#define dbgx( x ) {  } 
#define dbg( ... ) {  } 
#endif

void prepare(string s) {
#ifdef MY_DEBUG
	freopen("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#else
	//freopen("input.txt", "r", stdin);
	//freopen ("output.txt", "w", stdout);
#endif
}

const int N = 13;

string d[N][N][N][3];
int n, r, p, s;

int win[3][3] = {
  {-1, 0, 2},
  {0, -1, 1},
  {2, 1, -1}
};

void read() {
  scanf("%d %d %d %d", &n, &r, &p, &s);
}

string get(int p, int r, int s) {
  string res = d[p][r][s][0];
  forn(i, 3)
    if (d[p][r][s][i] != "")
      res = min(res, d[p][r][s][i]);
  return res;
}

void solve() {
  string res = get(p, r, s).c_str();
  if (res == "z")
    printf("IMPOSSIBLE\n");
  else
    printf("%s\n", res.c_str());
}

bool pow2(int n) {
  if (n == 0)
    return false;
  return (n & (n - 1)) == 0;
}

//string go(int p, int r, int s, int w) {
//  if (!pow2(p + r + s))
//    return "z";
//
//  if (d[p][r][s][w] != "z")
//    return d[p][r][s][w];
//
//  if (p + r + s == 1)
//    return "z";
//
//  forn(i, p + 1) {
//    forn(j, r + 1) {
//      forn(k, s + 1) {
//        if ((i + j + k) * 2 == (p + r + s)) {
//          string r1, r2;
//          forn(w1, 3) forn(w2, 3) {
//            if (win[w1][w2] == -1)
//              continue;
//            r1 = go(i, j, k, w1);
//            r2 = go(p - i, r - j, s - k, w2);
//            if (r1 == "z" || r2 == "z")
//              continue;
//            d[p][r][s][win[w1][w2]] = min(d[p][r][s][win[w1][w2]], r1 + r2);
//          }
//        }
//      }
//    }
//  }
//  return d[p][r][s][w];
//}
struct T {
  int p, r, s, w;
  T(int i, int j, int k, int _w) {
    p = i;
    r = j;
    s = k;
    w = _w;
  }
};
bool ok(const T &t) {
  return t.p < N && t.r < N && t.s < N;
}

void calc() {
  forn(i, N) forn(j, N) forn(k, N) forn(k2, 3) d[i][j][k][k2] = "z";
  d[1][0][0][0] = "P";
  d[0][1][0][1] = "R";
  d[0][0][1][2] = "S";
  
  vector<T> v;
  forn(n, N) {
    v.clear();
    dbgx(n);
    forn(i, N) {
      forn(j, N) {
        forn(k, N) {
          if (i + j + k != (1 << n)) continue;
          forn(w, 3) {
            if (d[i][j][k][w] != "z") {
              v.pb(T(i, j, k, w));
            }
          }
        }
      }
    }
    sort(all(v), [&](const T &a, const T &b) {
      return d[a.p][a.r][a.s][a.w] < d[b.p][b.r][b.s][b.w];
    });
    forn(i, sz(v)) {
      dbgx(i);
      forab(j, i + 1, sz(v) - 1) {
        T t(1, 1, 1, 1);
        t.p = v[i].p + v[j].p;
        t.r = v[i].r + v[j].r;
        t.s = v[i].s + v[j].s;
        t.w = win[v[i].w][v[j].w];
        if (!ok(t))
          return;
        if (d[t.p][t.r][t.s][t.w] == "z") {
          d[t.p][t.r][t.s][t.w] = d[v[i].p][v[i].r][v[i].s][v[i].w] + d[v[j].p][v[j].r][v[j].s][v[j].w];
        }
      }
    }
  }

  /*forn(i, N) {
    dbgx(i);
    forn(j, N) {
      dbgx(j);
      forn(k, N) {
        forn(k2, 3) {
          go(i, j, k, k2);
        }
      }
    }
  }*/
}

int main() {
	prepare("");

  calc();

  int t;
  scanf("%d", &t);
  forn(i, t) {
    printf("Case #%d: ", i + 1);
    read();
    solve();
  }
	dbg("Clock = %.3f\n", clock() / (double)CLOCKS_PER_SEC);
	return 0;
}
