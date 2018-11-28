#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
const int N = 205;
double p[N];
double f[N][N];
double calc(vector<double> t)
{
	memset(f, 0, sizeof(f));
	int m = t.size();
	f[0][0] = 1;
	for (int i = 1; i <= m; ++ i)
	{
		for (int j = 0; j <= i; ++ j)
		{
			f[i][j] = (1 - t[i - 1]) * f[i - 1][j];
			if (j) f[i][j] += t[i - 1] * f[i - 1][j - 1];
		}
	}
	return f[m][m / 2];
}
int main()
{
	int T, zzz = 0;
	scanf("%d", &T);
	while (T --)
	{
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++ i) scanf("%lf", &p[i]);
		sort(p + 1, p + 1 + n);
		double ans = 0;
		for (int i = 0; i <= m; ++ i)
		{
			vector<double> tmp;
			for (int j = 1; j <= i; ++ j) tmp.push_back(p[j]);
			for (int j = n; tmp.size() < m; -- j) tmp.push_back(p[j]);
			ans = max(ans, calc(tmp));
		}
		printf("Case #%d: %.10f\n", ++ zzz, ans);
	}
}

