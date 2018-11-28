#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int N, K;
double p[205], cp[205];
int a[205];
double ret;
int aa[205];
double table[205][105];

double solve(int cur, int yes)
{
	if (cur < 0)
	{
	  return (yes == 0) ? 1 : 0;
	}
	if (yes < 0)
	{
	  return 0;
	}

  if (table[cur][yes] > -0.5)
    return table[cur][yes];
	double ret = 0;
	ret = solve(cur - 1, yes - 1) * cp[cur] + solve(cur - 1, yes) * (1 - cp[cur]);
	return table[cur][yes] = ret;
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int cn = 1; cn <= T; ++cn)
  {
    scanf("%d%d", &N, &K);
    for (int i = 0; i < N; ++i)
      scanf("%lf", &p[i]);
    sort(p, p + N);
    ret = -1;

    for (int i = 0; i <= K; ++i)
    {
			for (int j = 0; j < i; ++j)
			{
			  cp[j] = p[j];
			}
			for (int j = i; j < K; ++j)
			{
			  cp[j] = p[(N - 1) - (j - i)];
			}
			for (int j = 0; j <= K; ++j)
			  for (int k = 0; k <= K / 2; ++k)
			    table[j][k] = -1;

			double tmp = solve(K - 1, K / 2);
			if (ret < tmp)
			  ret = tmp;
    }

    printf("Case #%d: %.10lf\n", cn, ret);
  }
}
