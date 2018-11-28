#include <cassert>
#include <cstring>

#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAXN = 1e6;

llint sums[MAXN];
int k;

int main(void) {
  int ntc; scanf("%d", &ntc);
  REP(tc, ntc) {
    printf("Case #%d: ", tc+1); fflush(stdout);

    int nn;
    scanf("%d %d", &nn, &k);
    int ns = nn-k+1;
    REP(i, ns) scanf("%lldd", sums+i);

    vector<pair<llint, llint> > ps;
    llint M = 0;
    for (int i = 0; i < k; ++i) {
      llint val = 0;
      llint mini = 0, maks = 0;

      for (int j = i; j+1 < ns; j += k) {
        val += sums[j+1] - sums[j];
        mini = min(mini, val);
        maks = max(maks, val);
      }

      ps.push_back(make_pair(mini, maks));
      M = max(M, maks - mini);
    }

    llint s0 = sums[0] % k;
    llint can_add = 0;
    for (auto p : ps) {
      s0 += p.first;
      can_add += M - (p.second - p.first);
    }
    s0 %= k; s0 += k; s0 %= k;
    if (can_add < s0) ++M;

    printf("%lld\n", M);
  }

  return 0;
}   
