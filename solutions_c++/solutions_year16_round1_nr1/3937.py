#include <bits/stdc++.h>

using namespace std;

char s[1010];

int main()
{
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc)
	{
		scanf("%s", s);
		int l = strlen(s);
		char mx = s[0];
		for (int i = 1; i < l; ++i)
		{
			mx = max(mx, s[i]);
		}
		string ans = "";
		ans += s[0];
		for (int i = 1; i < l; ++i)
		{
			if (ans[0] <= s[i] && s[i] <= mx)
			{
				ans = s[i] + ans;
			}
			else
			{
				ans += s[i];
			}
		}
		printf("Case #%d: %s\n", tc, ans.c_str());
	}
	return 0;
}