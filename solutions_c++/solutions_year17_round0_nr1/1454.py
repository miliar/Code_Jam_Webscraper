#include <bits/stdc++.h>
using namespace std;

int T, K, n, Ans;
char s[100001];

int main()
{
	
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++ Case)
	{
		printf("Case #%d: ", Case); Ans = 0;
		scanf("%s%d", s + 1, &K);
		n = strlen(s + 1);
		for (int i = n; i - K >= 0; -- i)
		{
			if (s[i] == '-')
			{
				++ Ans;
				for (int j = i - K + 1; j <= i; ++ j)
					if (s[j] == '-') s[j] = '+'; else s[j] = '-';
			}
		}
		int flag = 1;
		for (int i = 1; i <= n; ++ i)
			if (s[i] == '-') flag = 0;
		if (!flag) printf("IMPOSSIBLE\n");
		else printf("%d\n", Ans);
	}
	return 0;
}

