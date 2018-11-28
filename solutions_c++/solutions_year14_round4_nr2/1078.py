#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define TRACE(x) cout << #x << " = " << x << endl
#define REP(i, n) for (int i = 0; i < (n); ++i)

typedef long long llint;

const int MAXN = 1010;
const int inf = 1e9;

int a[MAXN], p[MAXN];
int f[MAXN];

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp) {
    int n;
    scanf("%d", &n);
    REP(i, n) scanf("%d", a+i);
    REP(i, n) p[i] = i;

    int ans = inf;
    do {
      int m = 0;
      REP(i, n)
        if (a[p[i]] > a[p[m]]) m = i;
      bool ok = true;
      REP(i, m)
        if (a[p[i]] > a[p[i+1]]) { ok = false; break; }
      for (int i = m+1; i < n; ++i)
        if (a[p[i]] > a[p[i-1]]) { ok = false; break; }
      if (!ok) continue;
      
      REP(i, n) f[i] = i;
      int cnt = 0;
      REP(i, n) {
        int w = i;
        while (f[w] != p[i]) w++;
        for (int j = w; j > i; --j)
          swap(f[j], f[j-1]), cnt++;
      }
      ans = min(ans, cnt);
    } while (next_permutation(p, p + n));

    printf("Case #%d: ", tp);
    printf("%d\n", ans);
  }
  return 0;
}
