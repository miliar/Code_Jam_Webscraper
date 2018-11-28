#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t, lt, rt, ans;
	string s;
	bool ok;
	scanf("%d", &t);
	for (int tt = 1;tt <= t;tt++)
	{
		ans = 0;ok = 1;
		cin >> s;
		for (int i = 0;i<s.size();i++)
			if (s[i] == '-')
				ok = 0;
		if (ok)
		{
			printf("Case #%d: %d\n", tt, ans);
			continue;
		}
		while (!ok)
		{
			lt = 0;
			rt = s.size() - 1;
			while (lt < s.size() && s[lt] == '+')
				lt++;
			if (lt != 0)
				ans++;
			while (rt >= 0 && s[rt] == '+')
				rt--;
			if (rt<0)
				break;
			while (lt<rt)
			{
				if (s[lt] == '-')
					s[lt] = '+';
				else
					s[lt] = '-';
				if (s[rt] == '-')
					s[rt] = '+';
				else
					s[rt] = '-';
				swap(s[lt], s[rt]);
				lt++;rt--;
			}
			if (lt == rt)
			{
				if (s[rt] == '-')
					s[rt] = '+';
				else
					s[rt] = '-';
			}
			ans++;
			ok = 1;
			for (int i = 0;i<s.size();i++)
				if (s[i] == '-')
					ok = 0;
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}