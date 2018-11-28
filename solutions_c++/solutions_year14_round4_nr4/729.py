#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

int n;
int place[10];
vector<string> strs;
int ans;
int xMax;

int check(int s)
{
	set<string> prefixes;
	for (size_t i = 0; i < strs.size(); ++i)
	{
		if (place[i] != s)
			continue;
		const string &s = strs[i];
		for (size_t j = 0; j <= s.size(); ++j)
		{
			prefixes.insert(s.substr(0, j));
		}
	}
	return (int)prefixes.size();
}

void put(int idx, int x)
{
	if (idx == strs.size())
	{
		int ret = 0;
		for (int i = 0; i < n; ++i)
		{
			int y = check(i);
			if (y == 0)
				return; // Empty server.
			ret += y;
		}
		if (ret == x)
		{
			++ans;
		}
		if (ret > xMax)
			xMax = ret;
		return;
	}
	for (int i = 0; i < n; ++i)
	{
		place[idx] = i;
		put(idx + 1, x);
	}
}

int main(void)
{
	int cases;
	cin >> cases;
	for (int t = 0; t < cases; ++t)
	{
		int m;
		cin >> m >> n;
		strs.resize(m);
		for (int i = 0; i < m; ++i)
			cin >> strs[i];
		xMax = 0;
		put(0, -1);
		ans = 0;
		put(0, xMax);

		cout << "Case #" << (t + 1) << ": " << xMax << ' ' << ans << endl;
	}
	return 0;
}
