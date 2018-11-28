#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	ll t, n, i, T, res, temp;
	string str;
	char rst;
	cin >> T;
	for (t = 1; t <= T; ++t)
	{
		cin >> str;
		rst = '+';
		res = 0;
		for (i = str.length()-1; i >= 0; --i)
		{
			if (str[i] != rst)
			{
				++res;
				if (rst == '+')
					rst = '-';
				else
					rst = '+';
			}
		}
		printf("Case #%lld: %lld\n", t, res);
	}
	return 0;
}