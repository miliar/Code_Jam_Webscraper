#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cout << "Case #" << tt << ": ";
		double c, f, x;
		cin >> c >> f >> x;
		cout.precision(7);
		double ans = 0.0;
		double prod = 2.0;
		while (true)
		{
			if (x / (prod + f) + c / (prod) < x / prod)
			{
				ans += c / prod;
				prod += f;
			}
			else break;
		}
		ans += x / prod;
		cout << fixed << ans << "\n";
	}
}