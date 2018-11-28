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
		int l = 0, r = strlen(s) - 1;

		int ans = 0;
		for (int i = 0; ; ++i)
		{
			while (r >= 0 && s[r] == '+')
			{
				--r;
			}
			if (r < 0) break;
			if (s[0] == '+')
			{
				int l = 0;
				while (l <= r && s[l] == '+')
				{
					s[l] = '-';
					++l;
				}
				++ans;
			}
			else
			{
				reverse(s, s + r + 1);
				for (int j = 0; j <= r; ++j)
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				++ans;
			}
		}

		printf("Case #%d: %d\n", tc, ans);
	}
}