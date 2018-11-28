#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define setmin(a,b) a = min(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define MP make_pair
#define A first
#define B second
#define RF(i,a,b) for(int i=(a)-1;i>=(b);--i)
#define BEND(v) (v).begin(),(v).end()
#define SZ(v) int((v).size())
#define FORI(i,v) FOR(i,SZ(v))
typedef long double ld;
typedef long long ll;

const int inf = 9999;
int R, C;
int grid[128][128];
int rowmax[128], colmax[128];
void doit(int cas) {
  bool ok = true;

  scanf(" %d %d", &R, &C);
  FOR(r,R) {
    FOR(c,C) {
      scanf(" %d", &grid[r][c]);
    }
  }

  FOR(r,R) rowmax[r] = 0;
  FOR(c,C) colmax[c] = 0;

  FOR(r,R) FOR(c,C) {
    rowmax[r] = max(rowmax[r], grid[r][c]);
    colmax[c] = max(colmax[c], grid[r][c]);
  }

  FOR(r,R) FOR(c,C) {
    if (grid[r][c] < rowmax[r] && grid[r][c] < colmax[c]) ok = false;
  }

  printf("Case #%d: %s\n", cas+1, ok ? "YES" : "NO");
}

int T;
int main() {
  scanf(" %d", &T);
  FOR(cas,T) doit(cas);
  return 0;
}
