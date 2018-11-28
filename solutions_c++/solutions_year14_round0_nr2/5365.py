#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

double c, f, x;

double can(double m)
{
	double cur = 2;
	double t = 0;
	while (t <= m)
	{
		if (cur * (m - t) >= x)
			return true;
		double need = c / cur;
		t += need;
		cur += f;
	}

	return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 0; t < tc; t++)
	{
		cin >> c >> f >> x;
		double l = 0;
		double r = x / 2;
		for (int i = 0; i < 200; i++)
		{
			double m = (l + r) / 2;
			if (can(m))
				r = m;
			else
				l = m;
		}
		printf("Case #%d: %.7lf\n", t + 1, l);
	}
}