/**         
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 * Date: 2014.06.14
 */

#include <cstdio>
#include <cassert>
#include <algorithm>
#include <iostream>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

typedef long long ll;

const int N = 1e7 + 100;

int n, p, q, r, s, a[N];
ll ma, sum[N + 1];

inline void relax( int a, int b )
{
  if (a <= b)
    ma = max(ma, sum[n] - max(max(sum[a], sum[b] - sum[a]), sum[n] - sum[b]));
}

void solve()
{
  cin >> n >> p >> q >> r >> s;
  forn(i, n)
    a[i] = ((ll)i * p + q) % r + s;
  forn(i, n)
    sum[i + 1] = sum[i] + a[i];

  // [0, a) [a, b) [b, n)
  ma = 0;
  int a = 0;
  forn(b, n + 1)
  {
    while (a < b && 2 * sum[a + 1] <= sum[b])
      a++;
    relax(a, b);
    relax(a + 1, b);
  }
  printf("%.10f\n", 1. * ma / sum[n]);
}

int main()
{
  int tn;
  scanf("%d", &tn);
  forn(t, tn)
  {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
