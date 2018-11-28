#include <stdio.h>
#include <algorithm>

int main()
{
	int T, c;
	int x, s[10005];
	int n, i, j, ans;

	scanf("%d", &T);
	for (c = 1; c <= T; c++)
	{
		scanf("%d %d", &n, &x);
		for (i = 0; i < n; i++)
			scanf("%d", &s[i]);
		std::sort(s, s+n);
		ans = n;
		for (i = 0, j = n - 1; i < j; i++, j--)
		{
			while (i < j && s[i] + s[j] > x) j--; 
			if (i >= j) break;
			ans--;
		}
		printf("Case #%d: %d\n", c, ans);
	}
	
	return 0;
}
