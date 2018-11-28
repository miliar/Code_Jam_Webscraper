#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
typedef vector<int> VI;
typedef pair<int, int> PII;
#define CLR(c,n) memset(c,n,sizeof(c))
template <class T> void checkmin(T &a, T b) { if (b<a) a=b; }
template <class T> void checkmax(T &a, T b) { if (b>a) a=b; }
#define TR(it, container) for(typeof(container.begin()) it = container.begin();\
it != container.end(); it++)
#define CONTAIN(it, container) (container.find(it)!=container.end())

typedef pair<int, int> PII;
bool mine[8][8], v[8][8];
bool validate(int n, int m, int x0, int y0) {
  CLR(v, 0);
  queue<PII> q;
  q.push(PII(x0, y0));
  v[x0][y0] = true;
  while (!q.empty()) {
    x0 = q.front().first; y0 = q.front().second; q.pop();
    bool has_mine = false;
    FOR(i, x0-1, x0+1) FOR(j, y0-1, y0+1) {
      if (i < 0 || i>= n || j < 0 || j >= m) continue;
      if (mine[i][j]) has_mine = true;
    }
    if (!has_mine) {
      FOR(i, x0-1, x0+1) FOR(j, y0-1, y0+1) {
	if (i < 0 || i>= n || j < 0 || j >= m || v[i][j]) continue;
	v[i][j] = true;
	q.push(PII(i, j));
      }
    }
  }
  REP(i, n) REP(j, m) if (!mine[i][j] && !v[i][j]) return false;
}
bool check(int n, int m, int c, bool output = false) {
  if (c < 0 || c >= n * m) return true;
  int M = 1 << (n * m);
  REP(mask, M) {
    if (__builtin_popcount(mask) != c) continue;
    int x = mask;
    CLR(mine, 0);
    REP(i, n) REP(j, m) {
      mine[i][j] = x & 1;
      x >>= 1;
    }
    REP(i, n) REP(j, m) if (!mine[i][j] && validate(n, m, i, j)) {
      if (output) {
	REP(i2, n) {
	  REP(j2, m) {
	    if (i == i2 && j == j2) printf("c");
	    else if (mine[i2][j2]) printf("*");
	    else printf(".");
	  }
	  printf("\n");
	}
      }
      return true;
    }
  }
  return false;
}
int main(int argc, char *argv[]) {
  /*
  FOR(n,1,5) FOR(m,1,n) REP(c, n*m) {
    bool ans = check(n, m, c);
    int l = n * m - c;
    if (m == 1 || n == 1 || c == 0 || l == 1) {
      assert(ans);
    } else if (l == 2 || l == 3) {
      assert(!ans);
    } else if (l % 2 == 0) {
      assert(ans);
    } else if (m == 2 || n == 2) {
      assert(!ans);
    } else if (l >= 9) {
      assert(ans);
    } else {
      assert(!ans);
    }
  }
  */
  int tc, n, m, c;
  cin >> tc;
  FOR(ic, 1, tc) {
    cin >> n >> m >> c;
    printf("Case #%d:\n", ic);
    if (!check(n, m, c, true)) printf("Impossible\n");
  }
}
