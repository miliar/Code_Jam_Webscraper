#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	int T, t, n, i;
	string s, res;
	cin >> T;
	for (t = 1; t <= T; ++t)
	{
		cin >> s;
		res = s[0];
		if (n == 1)
		{
			printf("Case #%d: %s\n", t, res.c_str());
			continue;
		}
		if (s[1] > s[0])
		{
			res = s[1]+res;
		}
		else
		{
			res = res+s[1];
		}
		++n;
		for (i = 2; i < s.length(); ++i)
		{
			if (res[0] <= s[i])
			{
				res = s[i] + res;
			}
			else
			{
				res = res + s[i];
			}
			++n;
		}
		printf("Case #%d: %s\n", t, res.c_str());
	}
	return 0;
}