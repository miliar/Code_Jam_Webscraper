#include "iostream"
#include "cstdio"
#include "cstdlib"
#include "string.h"

using namespace std;



char s[1005];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
	int T, cas = 0;
	scanf("%d",&T);
	while(T--)
	{
		cas++;
		int n;
		scanf("%s%d", s, &n);
		int len = strlen(s);
		int ans = 0;
		for (int i = 0; i < len - n + 1; i++)
		{
			if (s[i] == '+')
			{
				continue;
			}
			ans++;
			for (int j = 0; j < n; j++)
			{
				if (s[i+j] == '+') s[i+j] = '-';
				else s[i+j] = '+';
			}
		}
		bool ok = true;
		for (int i = len - n + 1; i < len; i++)
		{
			if (s[i] != '+')
			{
				ok = false;
				break;
			}
		}
		if (!ok)
		{
			printf("Case #%d: IMPOSSIBLE\n", cas);
		}
		else
		{
			printf("Case #%d: %d\n", cas, ans);
		}
	}
	return true;
}
