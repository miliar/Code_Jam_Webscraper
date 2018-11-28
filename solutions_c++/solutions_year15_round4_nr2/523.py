#include <iostream>

using namespace std;

const int MAXEACH = 1000000;
const long double MAXS = 1000000;
const int BINLOOP = 50;
const int DIVIDE = 10000;
const int MAXN = 100;

long double r[MAXN], c[MAXN];

int main()
{
	int tt;
	cin >> tt;
	for (int tc = 1; tc <= tt; tc++)
	{
		int n;
		long double v, x;
		cin >> n >> v >> x;
		for (int i = 0; i < n; i++)
			cin >> r[i] >> c[i];
		long double ans = -1;
		if (n == 1)
			if (c[0] == x)
				ans = v / r[0];
		if (n == 2)
		{
			if (c[0] == c[1])
			{
				if (c[0] == x)
					ans = v / (r[0] + r[1]);
			}
			else
			{
				long double a = (v * x - v * c[1]) / (c[0] - c[1]);
				if (a >= -1e-9 && a <= v + 1e-9)
				{
					long double b = v - a;
					ans = max(a / r[0], b / r[1]);
				}
			}
		}
		if (ans == -1)
			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
		else
		{
			cout.precision(9);
			cout << "Case #" << tc << ": " << fixed <<  ans << endl;
		}
	}
}
