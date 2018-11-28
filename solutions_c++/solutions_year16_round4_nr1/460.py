#include <cstdio>
#include <algorithm>
#include <type_traits>
using namespace std;

#define REP1(i, n) for (remove_cv<remove_reference<decltype(n)>::type>::type i = 1; i <= (n); i++)

int ri()
{
  int x;
  scanf("%d", &x);
  return x;
}

const long N = 4096;
char a[2][N+1];

void f(long k, long x)
{
  if (! k) return;
  switch (a[k&1][x]) {
  case 'P': a[k-1&1][2*x] = 'P'; a[k-1&1][2*x+1] = 'R'; break;
  case 'R': a[k-1&1][2*x] = 'R'; a[k-1&1][2*x+1] = 'S'; break;
  case 'S': a[k-1&1][2*x] = 'S'; a[k-1&1][2*x+1] = 'P'; break;
  }
  f(k-1, x*2);
  f(k-1, x*2+1);
}

void g(long l, long r)
{
  if (l == r-1) return;
  long m = (l+r)/2;
  g(l, m);
  g(m, r);
  if (! lexicographical_compare(a[0]+l, a[0]+m, a[0]+m, a[0]+r)) {
    rotate(a[0]+l, a[0]+m, a[0]+r);
  }
}

int main()
{
  long cases = ri(), k = 0, n, nn, P, R, S, PP, RR, SS;
  REP1(cc, cases) {
    n = 1 << ri();
    R = ri();
    P = ri();
    S = ri();

    printf("Case #%ld: ", cc);
    k = 0;
    for (nn = n, PP = P, RR = R, SS = S; nn > 1; nn /= 2) {
      long x = PP, y = RR, z = SS;
      PP = (x+y-z)/2;
      RR = (y+z-x)/2;
      SS = (z+x-y)/2;
      if (PP < 0 || RR < 0 || SS < 0) break;
      k++;
    }
    if (nn > 1)
      puts("IMPOSSIBLE");
    else {
      a[k&1][0] = PP ? 'P' : RR ? 'R' : 'S';
      f(k, 0);
      g(0, n);
      a[0][n] = '\0';
      puts(a[0]);
    }
  }
}
