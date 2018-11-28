/**
 * @author SCaffrey (srius.caffrey@gmail.com)
 * @date    2016-04-09 16:50:00
 * @copyright MIT
 */
#include <cstdio>// NOLINT
#include <cstring>// NOLINT
#include <bits/stdc++.h>// NOLINT
#include <cmath>// NOLINT
#define x1 x11
#define y1 y11

#define f(x, y, z) for (int x = (y), __ = (z); x < __; ++x)
#define g(x, y, z) for (int x = (y), __ = (z); x <= __; ++x)
#define fd(x, y, z) for (int x = (y), __ = (z); x > __; --x)
#define gd(x, y, z) for (int x = (y), __ = (z); x >= __; --x)

#ifdef WIN32
  #define LLD "%I64d"
  #define LLU "%I64u"
#else
  #define LLD "%lld"
  #define LLU "%llu"
#endif

typedef long long LL;// NOLINT
typedef long double real;

const double INF = 1e100;
const int oo = ~0u >> 2;
const double pi = acos(-1.0);
const double EPS = 1e-8;
const int MAXN = 100033;

int T;
int met[12];
int l;
int n, s;
inline void upd(int x) {
  while (x) {
    if (!met[x % 10]) --l;
    met[x % 10] = 1;
    x /= 10;
  }
}
void solve(int id) {
  printf("Case #%d: ", id);
  scanf("%d", &n);
  if (n == 0) {
    puts("INSOMNIA");
    return;
  }
  f(i, 0, 10) met[i] = 0;
  l = 10;
  s = 0;
  while (l && s <= 1e9) {
    s += n;
    upd(s);
  }
  if (l == 0) printf("%d\n", s);
  else puts("INSOMNIA");
}
int main() {
#ifdef LOCAL
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
#endif

  scanf("%d", &T);
  g(i, 1, T) {
    solve(i);
  }

#ifdef LOCAL
  fclose(stdin);
  fclose(stdout);
#endif
  return 0;
}

