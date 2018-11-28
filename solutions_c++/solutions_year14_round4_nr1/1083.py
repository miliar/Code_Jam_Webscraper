#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define TRACE(x) cout << #x << " = " << x << endl
#define REP(i, n) for (int i = 0; i < (n); ++i)

typedef long long llint;

const int MAXS = 707;

int a[MAXS];

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp) {
    int n, x;
    scanf("%d %d", &n, &x);
    REP(i, MAXS) a[i] = 0;
    REP(i, n) {
      int s;
      scanf("%d", &s);
      a[s]++;
    }

    int ans = 0;
    for (int i = MAXS-1; i >= 0; --i)
      while (a[i] > 0) {
        a[i]--;
        ans++;
        for (int j = i; j >= 0; --j)
          if (a[j] > 0 && j+i <= x) { a[j]--; break; }
      }

    printf("Case #%d: %d\n", tp, ans);
  }
  return 0;
}
