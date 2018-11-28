#include <iostream>

using namespace std;

void solve()
{
	int k, c, s;
	cin >> k >> c >> s;
	int need = k / c;
	if (k % c != 0) ++need;
	if (need > s) 
	{
		cout << " IMPOSSIBLE" << endl;
		return;
	}
	int now = 0;
	for(int i = 0; i < need; ++i)
	{
		unsigned long long tmp = 0;
		for (int j = 0; j < c; ++j)
		{
			if (now >= k) 
			{
				now = 0;
			}
			tmp = tmp * k + now;
			++now;
		}
		cout << " " << tmp + 1;
	}
	cout << endl;
}

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t; 
	for(int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ":";
		solve();
	}
	return 0;
}
