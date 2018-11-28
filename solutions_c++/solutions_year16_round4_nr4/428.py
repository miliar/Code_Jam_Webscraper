#include <algorithm>
#include <cstdio>
#include <type_traits>
using namespace std;

#define FOR(i, a, b) for (remove_cv<remove_reference<decltype(b)>::type>::type i = (a); i < (b); i++)
#define REP(i, n) FOR(i, 0, n)
#define REP1(i, n) for (remove_cv<remove_reference<decltype(n)>::type>::type i = 1; i <= (n); i++)

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

const long N = 5;
char a[N][N+1];
long uf[N*N], col[N], info[N*N];

long find(long x)
{
  while (uf[x] >= 0) {
    if (uf[uf[x]] >= 0)
      uf[x] = uf[uf[x]];
    x = uf[x];
  }
  return x;
}

void union_(long x, long y)
{
  x = find(x);
  y = find(y);
  if (x != y) {
    info[x] |= info[y];
    uf[x] += uf[y];
    uf[y] = x;
  }
}

int main()
{
  long cases = ri(), k, n, s = 0;
  REP1(cc, cases) {
    s = 0;
    n = ri();
    long all = (1 << n*n) - 1, ans = n*n;
    REP(i, n) {
      scanf("%s", a[i]);
      REP(j, n)
        if (a[i][j] == '1')
          s |= 1 << (i*n+j);
    }
    for (long m = all-s; ; m = m-1 & all-s) {
      long ss = m | s;
      fill_n(uf, n*n, -1);
      fill_n(info, n*n, 0);
      fill_n(col, n, -1);
      REP(i, n) {
        long row = -1;
        REP(j, n)
          if (1 << i*n+j & ss) {
            info[i*n+j] = 1 << n+i | 1 << j;
            if (col[j] >= 0) {
              union_(i*n+j, col[j]);
            }
            if (row >= 0) {
              union_(i*n+j, row);
            }
            row = i*n+j;
            col[j] = i*n+j;
          }
      }
      bool tak = true;
      long sum = 0, num = n;
      REP(i, n*n)
        if (uf[i] < 0 && info[i]) {
          long x = __builtin_popcount(info[i] >> n),
               y = __builtin_popcount(info[i] & (1<<n)-1);
          if (x != y || x*y != -uf[i]) {
            tak = false;
            break;
          }
          num -= x;
        }
      if (tak)
        ans = min(ans, (long)__builtin_popcount(m)+num);

      if (m == 0) break;
    }

    printf("Case #%ld: %ld\n", cc, ans);
  }
}
