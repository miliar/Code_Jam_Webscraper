#include <limits>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
#include <queue>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; ++i)
#define REP(i,n) for (int i = 1; i <= n; ++i)

long N;
long t[10000000];

void init()
{
  scanf(" %ld", &N);
  FOR(i, N*10) t[i] = 0;
}

long rev(long n)
{
  int ds[20];
  FOR (i,20) {
    ds[i] = n % 10;
    n /= 10;
  }

  int i = 1;
  long m = 0;
  long base = 1;
  while (!ds[20 - i]) ++i;
  for (;i <= 20; ++i) {
    m += ds[20 - i] * base;
    base *= 10;
  }

  return m;
}

long solve()
{
  init();

  typedef pair<long, int> P;
  queue<P> q;
  q.push(make_pair(1L, 1));

  while (!q.empty()) {
    P p = q.front();
    q.pop();
    if (p.first >= N*10 || t[p.first] > 0) continue;
    t[p.first] = p.second;
    if (p.first == N) break;
    q.push(make_pair(p.first + 1L, p.second + 1));
    q.push(make_pair(rev(p.first), p.second + 1));
  }

  return t[N];
}

int main()
{
  int ncases;
  scanf(" %d", &ncases);
  REP(i, ncases)
    printf("Case #%d: %ld\n", i, solve());

  return 0;
}
