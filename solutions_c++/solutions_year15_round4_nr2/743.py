#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <iostream>
#include <algorithm>
#include <deque>
#include <stack>
#include <fstream>
#include <string>
#include <cmath>
#include <climits>
#include <queue>
#include <ctime>
#include <functional>
#include <cstring>
#include <map>
#include <cctype>
#include <unordered_map>

using namespace std;
using pr = pair<double, double>;

double solve(vector<pr> a, double v, double x)
{
	if (a.size() == 2 && (a[0].second == x || a[1].second == x))
	{
		if (a[0].second == a[1].second)
		{
			a = vector<pr>(1, { a[0].first + a[1].first, a[0].second });
		}
		else
		{
			if (a[0].second == x)
				a = vector<pr>(1, a[0]);
			else
				a = vector<pr>(1, a[1]);
		}
	}

	if (a.size() == 1)
	{
		if (a[0].second == x)
		{
			return v / a[0].first;
		}
		return -1;
	}

	double t0 = a[0].second - x;
	double t1 = a[1].second - x;

	if (t0 * t1 < 0)
	{
		double r0 = (v * t1) / ((t1 - t0) * a[0].first);
		double r1 = (v * t0) / ((t0 - t1) * a[1].first);
		return max(r0, r1);
	}
	
	return -1;
}

int main()
{
	freopen("INPUT.TXT", "r", stdin); freopen("OUTPUT.TXT", "w", stdout);
	int t, n;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int n;
		double v, x;
		cin >> n >> v >> x;
		vector<pr> a(n);
		for (int u = 0; u < n; u++)
		{
			cin >> a[u].first >> a[u].second;
		}
		
		cout << "Case #" << i + 1 << ": ";
		double res = solve(a, v, x);
		if (res < -0.5)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			printf("%0.9f\n", res);
		}
	}
}