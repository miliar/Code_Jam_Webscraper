#include <cstdio>
#include <algorithm>

using namespace std;

double c,f,x;

inline double solve () {
  scanf ("%lf %lf %lf", &c, &f, &x);

  double cookie = 2,ans = -1u/2,sum = 0;
  while (sum < ans) {
    ans = min (ans, sum+x/cookie);
    sum += c/cookie;
    cookie += f;
  }
  return ans;
}

int main () {
  int test;
  scanf ("%d", &test);

  for (int i = 1;i <= test;i ++) {
    printf ("Case #%d: %.7lf\n", i, solve ());
  }
}
