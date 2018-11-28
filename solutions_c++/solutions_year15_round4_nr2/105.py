#include <bits/stdc++.h>

using namespace std;

typedef long double LD;

const int N = 10000;

LD speed[N], temp[N], coef[N], T, V;
int n;

inline int sgn (LD x) { return fabs(x) < 1e-9 ? 0 : x > 0 ? 1 : -1; }

void solve ()
{
	cin >> n >> V >> T;
	LD myV = 0;
	int m = 0;
	for (int i = 1; i <= n; ++i)
	{
		LD s, t;
		cin >> s >> t;
		LD coe = s * (t - T);
		if (sgn(coe) != 0)
		{
			coef[++m] = coe;
			speed[m] = s;
			temp[m] = t;
		}
		else
		{
			myV += s;
		}
	}
	LD bestV = 0;
	for (int i = 1; i <= m; ++i)
	{
		LD res = 0, curV = 0;
		for (int j = 1; j <= m; ++j)
			if (j != i)
			{
				res -= coef[j];
				curV += speed[j];
			}
		res /= coef[i];
		if (sgn(res) >= 0 && sgn(1 - res) >= 0)
		{
			curV += res * speed[i];
			if (sgn(curV - bestV) > 0) bestV = curV;
		}
	}
	if (sgn(bestV + myV) <= 0)
	{
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	cout.setf(ios::fixed);
	cout << setprecision(10) << V / (myV + bestV) << endl;
}

int main ()
{
	int tk;
	cin >> tk;
	for (int i = 1; i <= tk; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
