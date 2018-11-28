#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
using namespace std;

#define max2(a,b) (((a) > (b)) ? (a) : (b))
#define min2(a,b) (((a) < (b)) ? (a) : (b))

#define debug(x) cout << (#x) << ": " << (x) << endl
#define echo(x) cout << (#x) << endl
#define TIMER_A(timer) int timer = clock()
#define TIMER_B(timer) cerr << (#timer) << ": " << (double)(clock() - timer) / CLOCKS_PER_SEC << endl

typedef long long LL;
const double eps = 1e-9;
const double pi = M_PI;
const int inf = 2000000000; // 2e9
const LL inf64 = 9000000000000000000LL; // 9e18

int TC, TN;
LL R, T;

LL solve ()
{
  double x = floor((1 - 2.0 * R + sqrt(4.0 * R * R - 4.0 * R + 1 + 8.0 * T)) / 4);
  LL l = (LL)floor(x * 0.9), r = (LL)ceil(x * 1.1) + 1;
  while (r - l > 1)
  {
    LL n = (l + r) / 2;
    if ((2 * R + 1) * n + 2 * (n - 1) * n <= T)
      l = n;
    else
      r = n;
  }
  return l;
}

int main ()
{
  scanf("%d", &TN);
  for (TC = 1; TC <= TN; ++TC)
  {
    scanf("%lld%lld", &R, &T);
    printf("Case #%d: %lld\n", TC, solve());
  }
}
