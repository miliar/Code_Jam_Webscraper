#include <bits/stdc++.h>

#define MOD 1000000007

using namespace std;

typedef long long int lld;
typedef pair<int, int> pii;
typedef pair<pii, pii> line;

#define F first
#define S second
#define MN 305

double p[MN];
double dp[MN][MN];
int dpc[MN][MN];
int ch[MN];
int n, k;

double calc2(int pl, int pos)
{
  if (pos < 0)
    return 0;

  if (pl == k)
    return pos == 0;

  if (dpc[pl][pos] != -1)
    return dp[pl][pos];
  dpc[pl][pos] = 1;

  double ans = calc2(pl + 1, pos - 1) * p[ch[pl]] + calc2(pl + 1, pos) * (1 - p[ch[pl]]);

  return dp[pl][pos] = ans;
}

double calc(int cur, int pl)
{
  if (pl == k)
  {
    memset(dpc, -1, sizeof dpc);
    return calc2(0, k / 2);
  }

  if (cur == n)
    return 0;

  double v = calc(cur + 1, pl);
  ch[pl] = cur;
  v = max(v, calc(cur + 1, pl + 1));
  return v;
}

int main()
{
  int t, T, i;
  scanf("%d", &T);

  for (t = 1; t <= T; t++)
  {
    scanf("%d %d", &n, &k);

    for (i = 0; i < n; i++)
      scanf("%lf", &p[i]);

    sort(p, p + n);
    for (i = 0; i < k; i++)
      ch[i] = i;
    memset(dpc, -1, sizeof dpc);
    double ans = calc2(0, k / 2);

    for (i = 0; i < k; i++)
    {
      ch[k - i - 1] = n - i - 1;
      memset(dpc, -1, sizeof dpc);
      ans = max(ans, calc2(0, k / 2));
    }

    printf("Case #%d: %0.10lf\n", t, ans);
  }
  
  return 0;
}
