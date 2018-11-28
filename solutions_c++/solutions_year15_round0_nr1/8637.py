#include <stdio.h>

int main()
{

	int T;
	scanf("%d", &T);
	for (int cnt = 1; cnt <= T; cnt++)
	{
		int now = 0;
		int add = 0; 
		int level = 0;
		int t = 0;
		int n = 0;
		scanf("%d", &n);
		scanf("%1d", &now);
		for (int level = 1; level <= n; level++)
		{
			scanf("%1d", &t);
			if ((now + add) < level)
				add += (level - now - add);
			now += t;
		}
		printf("Case #%d: %d\n", cnt, add);
	}
}
