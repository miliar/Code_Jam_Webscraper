#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
 
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

#define frr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define fr(a,b) frr(a,0,b)
#define rp fr
#define ms(a,b) memset((a), (b), sizeof(a))
#define cl ms
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)
#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<

const int INF = 0x3f3f3f3f;
typedef long long ll;

using namespace std;

struct path{
  int d, c;
  path(int d = 0, int c = 0): d(d), c(c) {}
  bool operator<(const path &p2) const { return c > p2.c; }
};

#define mxb 1009
int w, h, b, n, dist[mxb][mxb], bx[mxb], ex[mxb], by[mxb], ey[mxb];

int fdist(int x, int y) {
  if (bx[x] <= ex[y] && bx[y] <= ex[x]) return max(by[x] - ey[y], by[y] - ey[x])-1;
  if (by[x] <= ey[y] && by[y] <= ey[x]) return max(bx[x] - ex[y], bx[y] - ex[x])-1;
  return max(max(by[x] - ey[y], by[y] - ey[x]), max(bx[x] - ex[y], bx[y] - ex[x]))-1;
}

bool mark[mxb];

int djikstra() {
  priority_queue<path> heap;
  path aux;
  heap.push(path(0, 0));
  ms(mark, 0);
  while (!heap.empty()) {
    aux = heap.top(); heap.pop();
    int v = aux.d;
    if (v == b+1) return aux.c;
    if (mark[v]) continue;
    mark[v] = 1;
    fr(x, n) if (!mark[x]) heap.push(path(x, aux.c + dist[v][x]));
  }
  return -1;
}

int main() {
  int t, cn = 1;
  sc(t);
  while (t--) {
    sc2(w, h); sc(b);
    n = b+2;
    fr(x, n) dist[x][x] = 0;
    dist[0][b+1] = dist[b+1][0] = w;
    fr(x, b) {
      sc2(bx[x], by[x]);
      sc2(ex[x], ey[x]);
      dist[0][x+1] = dist[x+1][0] = bx[x];
      dist[b+1][x+1] = dist[x+1][b+1] = w-1-ex[x];
    }
    fr(x, b) frr(y, x+1, b) dist[x+1][y+1] = dist[y+1][x+1] = fdist(x, y);
/*    fr(x, n) {
      fr(y, n) printf("%d ", dist[x][y]);
      puts("");
    }*/
    printf("Case #%d: ", cn++);
    pri(djikstra());
  }
  return 0;
}

