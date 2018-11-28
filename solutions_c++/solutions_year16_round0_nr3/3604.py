/**
 * @author SCaffrey (srius.caffrey@gmail.com)
 * @date    2016-04-09 17:43:17
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

LL T;
LL n, j;
LL a[33];
LL num;
LL b[33];
bool wtf() {

}
void check() {
  LL s = 0;
  g(u, 2, 10) {
    s = 0;
    g(i, 1, n) {
      s = s * u + a[i];
    }
    b[u] = 0;
    // if (s == 61) wtf();
    // printf("%lld:", s);
    f(i, 2, s) {
      if ((LL)i * i > s) return;
      if (s % i == 0) {
        b[u] = i; 
      // printf(" %lld\n", b[u]);
        break;
      }
    }
    if (b[u] == 0) return;
  }
  g(i, 1, n) printf("%lld", a[i]);
  g(i, 2, 10) printf(" %lld", b[i]);
  puts("");
  ++num;
}
void dfs(LL x) {
  if (num == j) return;
  if (x == n + 1) {
    check();
    return;
  }
  if (num == j) return;
  a[x] = 1;
  dfs(x + 1);
  if (x == 1 || x == n) return;
  if (num == j) return;
  a[x] = 0;
  dfs(x + 1);
}
int main() {
#ifdef LOCAL
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
#endif

  scanf("%lld%lld%lld", &T, &n, &j);
  puts("Case #1:");
  dfs(1);

#ifdef LOCAL
  fclose(stdin);
  fclose(stdout);
#endif
  return 0;
}

