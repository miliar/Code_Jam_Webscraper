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
    int n, x; scanf("%d %d", &n, &x);

    multiset<int> left;
    REP(i, n) {
      int x; scanf("%d", &x);
      left.insert(x);
    }

    int ans = 0;
    while (left.size() > 0) {
      int a = *left.rbegin(); left.erase(--left.end());
      auto it = left.upper_bound(x - a);
      if (it != left.begin()) {
        --it;
        left.erase(it);
      }
      ++ans;
    }

    printf("Case #%d: %d\n", tc+1, ans);
    fflush(stdout);
  }
  return 0;
}
