#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	freopen("", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	cin >> t;
	for (int j = 0; j < t; j++)
	{
		int s_max;
		string s;
		cin >> s_max >> s;
		int cur = 0;
		int ans = 0;
		for (int i = 0; i < (int)s.size(); i++)
		{
			if (cur >= i)
			{
				cur += s[i] - '0';
			}
			else
			{
				ans += i - cur;
				cur = i + s[i] - '0';
			}
		}
		cout << "Case #" << j + 1 << ": " << ans << endl;
	}

	return 0;
}
