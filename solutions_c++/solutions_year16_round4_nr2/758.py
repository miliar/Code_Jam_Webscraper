	//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 212;
typedef long long ll;

double *dp[N];
double p[N], q[N];

double get(int n, double *p, double *q)
{
	int km = n/2;
	dp[0][0] = 1;		
	for(int i = 1; i <= n; i++)
		for(int dif = -km - 1; dif <= km + 1; dif++)
			dp[i][dif] = 0;
	for(int i = 1; i <= n; i++)
		for(int dif = max(-km, -i); dif <= min(km, i); dif++)
		{
			double &cur = dp[i][dif];
			cur = dp[i - 1][dif - 1] * p[i];
			cur += dp[i - 1][dif + 1] * q[i];
		}
	return dp[n][0];
}

int main()
{
	int _t = in();
	for(int i = 0; i < N; i++)
		dp[i] = (new double[N] + N/2);
	for(int t = 1; t <= _t; t++)
	{
		cout << "Case #" << t << ": ";
		int n = in(), k = in();
		for(int i = 1; i <= n; i++)
		{
			cin >> p[i];
			q[i] = 1.0 - p[i];
		}
		double _p[k], _q[k];
		double ans = 0;
		for(int mask = 0; mask < (1 << n); mask++)
		{
			if(__builtin_popcount(mask) != k)
				continue;
			int chi = 0;
			for(int i = 0; i < n; i++)
				if(mask >> i & 1)
				{
					_p[++chi] = p[i + 1];
					_q[chi] = q[i + 1];
				}
			ans = max(ans, get(k, _p, _q));
		}
		cout << setprecision(10) << fixed << ans << endl;
	}
}
