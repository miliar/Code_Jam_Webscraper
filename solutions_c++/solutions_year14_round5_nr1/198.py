#include <cassert>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <set>

using namespace std;

#define REP(i, n) FOR(i, 0, n)
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

int main(void)
{
  int ntc; scanf("%d", &ntc);
  REP(tc, ntc) {
    int n, p, q, r, s; scanf("%d %d %d %d %d", &n, &p, &q, &r, &s);
    vector<int> A(n);
    REP(i, n) A[i] = (i*(llint)p + q) % r + s;
    
    const int MAXN = 1e6 + 123;
    static llint prefix[MAXN];
    REP(i, n+1)
      if (i == 0) prefix[i] = 0;
      else prefix[i] = prefix[i-1] + A[i-1];

    llint ans = 1e18;
    for (int p = 0; p < n; ++p) {
      int lo = p, hi = n-1;
      llint S = prefix[n] - prefix[p];
      while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (S - 2*(prefix[mid] - prefix[p]) >= 0)
          lo = mid;
        else 
          hi = mid - 1;
      }
      int mid = lo;
      llint val = min( max(prefix[mid]-prefix[p], prefix[n]-prefix[mid]),
                       max(prefix[mid+1]-prefix[p], prefix[n]-prefix[mid+1]) );
      ans = min(ans, max(prefix[p] - prefix[0], val));
    }
    
    printf("Case #%d: %.12lf\n", tc+1, (prefix[n] - ans) / double(prefix[n]));
    fflush(stdout);
  }
  return 0;
}
