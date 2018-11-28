#ifdef _MSC_VER
typedef __int32 int32_t;
typedef unsigned __int32 uint32_t;
typedef __int64 int64_t;
typedef unsigned __int64 uint64_t;
#define PRId64 "I64d"
#define SCNd64 PRId64
#else
#define __STDC_FORMAT_MACROS
#include <inttypes.h>
#include <stdint.h>
#endif
#include <algorithm>
#include <climits>
#include <cstring>
#include <cstdio>
#include <functional>
#include <map>
#include <set>
#include <utility>
#include <queue>
#include <vector>
using namespace std;
typedef int64_t i64;
typedef unsigned u;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define REP1(i, n) for (int i = 1; i <= (n); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define ROF(i, a, b) for (int i = (b); --i >= (a); )
#define pb push_back
#define mp make_pair
#define fi first
#define se second
typedef double ft;

typedef vector<int> VI;
typedef pair<int, int> PII;

int ri()
{
  int x;
  scanf("%d", &x);
  return x;
}

double rd()
{
  double x;
  scanf("%lf", &x);
  return x;
}

i64 rl()
{
  i64 x;
  scanf("%" SCNd64, &x);
  return x;
}

const int W = 100, H = 500, V = W*H*2+2;
bool a[W][H];

bool f(int w, int h)
{
  queue<PII> q;
  REP(c, w)
    if (a[c][0])
      q.push(PII(c,0));
  while (! q.empty()) {
    PII x = q.front();
    q.pop();
    if (x.se == h-1) {
      return true;
      break;
    }
  }
  return true;
}

int he[V], nh[V+1], src, sink;
struct Edge {
  int v, c;
  Edge *next, *pair;
} *e[V], pool[4*W+5*W*H << 1], *pit;

int augment(int u, int d)
{
  if (u == sink)
    return d;
  int old = d, minh = sink;
  for (Edge *it = e[u]; it; it = it->next)
    if (it->c > 0) {
      if (he[u] == he[it->v]+1) {
        int dd = augment(it->v, min(d, it->c));
        it->c -= dd;
        it->pair->c += dd;
        if (!(d -= dd)) break;
      }
      minh = min(minh, he[it->v]);
    }
  if (old == d) {
    if (!--nh[he[u]]) he[src] = sink+1;
    minh = max(minh, he[u]);
    nh[he[u] = minh+1]++;
  }
  return old-d;
}

void insert(int u, int v, int c)
{
  *pit = (Edge){v, c, e[u], pit+1}; e[u] = pit++;
  *pit = (Edge){u, 0, e[v], pit-1}; e[v] = pit++;
}

int main()
{
  int cases = ri();
  REP1(cc, cases) {
    int w = ri(), h = ri(), b = ri();
    memset(a, 0, sizeof a);
    REP(i, b) {
      int x = ri(), y = ri(), xx = ri(), yy = ri();
      FOR(c, x, xx+1)
        FOR(r, y, yy+1)
          a[c][r] = true;
    }

#define f(i,j,k) (((j)*w+(i))*2+(k))

    src = 2*w*h;
    sink = src+1;
    fill_n(e, sink+1, nullptr);
    pit = pool;
    REP(i, w) {
      if (! a[i][0]) {
        insert(src, f(i,0,0), 1);
        insert(f(i,0,0), f(i,0,1), 1);
      }
      if (! a[i][h-1]) {
        insert(f(i,h-1,1), sink, 1);
        insert(f(i,h-1,0), f(i,h-1,1), 1);
      }
    }

    REP(i, w)
      REP(j, h)
        if (! a[i][j] ) {
          if (i && ! a[i-1][j]) insert(f(i,j,1), f(i-1,j,0), 1);
          if (i+1 < w && ! a[i+1][j]) insert(f(i,j,1), f(i+1,j,0), 1);
          if (j && ! a[i][j-1]) insert(f(i,j,1), f(i,j-1,0), 1);
          if (j+1 < h && ! a[i][j+1]) insert(f(i,j,1), f(i,j+1,0), 1);
          insert(f(i,j,0), f(i,j,1), 1);
        }

    int flow = 0;
    fill_n(he, sink+1, 0);
    fill_n(nh, sink+2, 0);
    while (he[src] < sink+1)
      flow += augment(src, INT_MAX);
    printf("Case #%d: %d\n", cc, flow);
  }
}
