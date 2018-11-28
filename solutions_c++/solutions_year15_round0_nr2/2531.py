#include <iostream>
#include <vector>

using namespace std;

int solve(vector<int>& d, int c)
{
	int ret = 0;
	int pos = 0;
	for (int i = 0; i < c; ++i)
	{
		if (d[i] >= ret)
		{
			ret = d[i];
			pos = i;
		}
	}
	if (ret <= 2)
	{
		return ret;
	}
	// d[pos] = ret / 2;
	// d.push_back(ret - ret / 2);
	// int tmp = solve(d, c + 1) + 1;
	// d[pos] = ret;
	// d.resize(c);
	// return min(ret, tmp);
	int maxp = ret;
	for (int i = 2; i <= (maxp/2); ++i)
	{
		d[pos] = maxp / i;
		d.push_back(maxp - maxp / i);
		ret = min(solve(d, c+1)+1, ret);
		d[pos] = maxp;
		d.resize(c);
	}
	return ret;
}

int main()
{
	int t, d;
	cin >> t;
	for (int cc = 1; cc <= t; ++cc)
	{
		cin >> d;
		vector<int> p(d, 0);
		int result = 0;
		for (int i = 0; i < d; ++i)
		{
			cin >> p[i];
		}
		result = solve(p, d);
		cout << "Case #" << cc << ": " << result << endl;
	}
	return 0;
}