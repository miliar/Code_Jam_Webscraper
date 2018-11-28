#include <bits/stdc++.h>
using namespace std;
#define MAX 1005
char str[MAX];
int main()
{
	int t, n, tot, res;
	scanf("%d", &t);
	for (int tt = 1; tt<= t; tt++)
	{
		tot = res = 0;
		scanf("%d%s", &n,str);
		for (int i = 0;i <= n; i++)
		{
			if (tot < i)
			{
				res += (i - tot);
				tot = i;
			}
			tot += str[i] - '0';
		}
		printf("Case #%d: %d\n", tt, res);
	}
}