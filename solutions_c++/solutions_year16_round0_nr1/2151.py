#include <cstdio>
#include <cstring>

bool appear[10];

int main()
{
	int T, n;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt)
	{
		scanf("%d", &n);
		printf("Case #%d: ", tt);
		if (n == 0)
		{
			puts("INSOMNIA");
			continue;
		}
		int x = 0, tot = 0;
		memset(appear, 0, sizeof appear);
		while (true)
		{
			x += n;
			for (int y = x; y; y /= 10)
				if (!appear[y % 10])
				{
					++tot;
					appear[y % 10] = true;
				}
			if (tot == 10) break;
		}
		printf("%d\n", x);
	}
	return 0;
}
