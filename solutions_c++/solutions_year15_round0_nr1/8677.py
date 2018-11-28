#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int t, n, ans;
char s[1005];

int main()
{
	scanf("%d", &t);
	int tm, num;
	for (int cas = 1; cas <= t; cas++)
	{
		scanf("%d %s", &n, s);
		num = ans = 0;
		for (int i = 0; i <= n; i++)
		{
			tm = (int)(s[i]-'0');
			if (tm != 0 && i > num)
			{
				ans += i - num;
				num += i - num;
			}
			num += tm;	
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}