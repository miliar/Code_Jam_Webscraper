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

int TN, TC;

int N, P;

void input ()
{
  scanf("%d%d", &N, &P);
}

int worstRank (int t)
{
  int rk = 0;
  int rm = t;
  for (int i = 0; i < N; ++i)
  {
    rk = rk << 1 | bool(rm);
    rm = (rm - 1) / 2;
  }
  return rk;
}

int bestRank (int t)
{
  int rk = 0;
  int rm = (1 << N) - t - 1;
  for (int i = 0; i < N; ++i)
  {
    rk = rk << 1 | !bool(rm);
    rm = (rm - 1) / 2;
  }
  return rk;
}

int solve1 ()
{
  for (int i = (1 << N) - 1; i >= 0; --i)
    if (worstRank(i) < P)
      return i;
}

int solve2 ()
{
  for (int i = (1 << N) - 1; i >= 0; --i)
    if (bestRank(i) < P)
      return i;
}

void solve ()
{
  printf("%d %d\n", solve1(), solve2());
}

int main ()
{
  scanf("%d ", &TN);
  for (TC = 1; TC <= TN; ++TC)
  {
    input();
    printf("Case #%d: ", TC);
    solve();
  }
}
