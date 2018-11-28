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
#define mp make_pair

const int N = 100;
const int H = 200;
const int MIN = 20;
const int EXTRA = N * H / MIN + 1;

int p, q, n, g[N], h[N + 1];
int m[N][H + 1][EXTRA];
int cc, u[N][H + 1][EXTRA];

inline int go( int i, int hp, int extra, int who )
{
  if (i == n)
    return 0;
  if (!who)
  {
    if (hp <= 0)
      return go(i + 1, h[i + 1], extra, 0) + g[i];
    if (!extra)
      return go(i, hp, 0, 1);
    assert(i < N);
    assert(hp <= H);
    assert(extra < EXTRA);
    if (u[i][hp][extra] == cc)
      return m[i][hp][extra];
    u[i][hp][extra] = cc;
    return m[i][hp][extra] = max(
      go(i, hp - p, extra - 1, 0),
      go(i, hp, extra, 1)
    );
  }
  else
  {
    hp -= q;
    if (hp <= 0)
      i++, hp = h[i];
    return go(i, hp, extra + 1, 0);
  }
}

void solve()
{
  cin >> p >> q >> n;
  forn(i, n)
    cin >> h[i] >> g[i];
  cc++;
  printf("%d\n", go(0, h[0], 1, 0));
}

int main()
{
  int tn;
  scanf("%d", &tn);
  forn(t, tn)
  {
    fprintf(stderr, "Case #%d:\n", t + 1);
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
