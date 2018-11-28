/**
 * @author SCaffrey (srius.caffrey@gmail.com)
 * @date    2016-04-09 17:35:07
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
char s[133];
int len;
void flip(int x) {
  f(i, 0, x) s[i] = '-' + '+' - s[i];
}
int ans;
void solve(int id) {
  printf("Case #%d: ", id);
  scanf("%s", s);
  len = strlen(s);
  ans = 0;
  f(i, 1, len) {
    if (s[i] != s[i - 1]) {
      flip(i);
      ++ans;
    }
  }
  if (s[len - 1] == '-') ++ans;
  printf("%d\n", ans);
}
int main() {
#ifdef LOCAL
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
#endif

  scanf("%d", &T);
  g(i, 1, T) solve(i);

#ifdef LOCAL
  fclose(stdin);
  fclose(stdout);
#endif
  return 0;
}

