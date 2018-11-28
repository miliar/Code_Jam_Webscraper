#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int T, cas = 0;
	cin >> T;
	while (T--)
	{
		int n;
		string s;
		cin >> n >> s;
		int ans = 0;
		int cur = s[0] - '0';
		for (int i = 1; i <= n; ++i)
		{
			if (cur >= i) cur += s[i] - '0';
			else 
			{
				int tmp = i - cur;
				ans += tmp;
				cur += s[i] - '0' + tmp;
			}
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}
