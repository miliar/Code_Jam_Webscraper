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

const long N = 201;
double a[N], b[N], c[N];

int main()
{
  long cases = ri(), k, n;
  REP1(cc, cases) {
    n = ri();
    k = ri();
    REP(i, n)
      a[i] = rd();
    sort(a, a+n);
    double ans = 0;
    REP(x, k+1) {
      long y = k-x;
      fill_n(b, n+1, 0.0);
      b[0] = 1;
      REP(i, x) {
        fill_n(c, n+1, 0.0);
        REP(j, n+1) {
          c[j] += b[j] * (1-a[i]);
          c[j+1] += b[j] * a[i];
        }
        copy_n(c, n+1, b);
      }
      REP(i, y) {
        fill_n(c, n+1, 0.0);
        REP(j, n+1) {
          c[j] += b[j] * (1-a[n-1-i]);
          c[j+1] += b[j] * a[n-1-i];
        }
        copy_n(c, n+1, b);
      }
      ans = max(ans, b[k/2]);
    }

    printf("Case #%ld: %lf\n", cc, ans);
  }
}
