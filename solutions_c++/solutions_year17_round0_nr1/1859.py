#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int a[100500];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		string s;
		int k;
		cin >> s >> k;
		for (int j = 0; j < s.length(); ++j)
		{
			if (s[j] == '-')
			{
				a[j] = 1;
			}
			else
			{
				a[j] = 0;
			}
		}
		int ans = 0;
		for (int j = 0; j < s.length(); ++j)
		{
			if (a[j] == 1)
			{
				if (j + k > s.length())
				{
					ans = -1;
					break;
				}
				ans++;
				for (int u = 0; u < k; ++u)
				{
					a[j + u] = 1 - a[j + u];
				}
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if (ans == -1)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << ans << endl;
		}
	}
	return 0;
}
