#include <cstdio>
#include <cstring>
char cake[105];

int main(void)
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		int len, count = 0, i = 0;
		scanf("%s", cake);
		len = strlen(cake);
		bool smile = true;
		if (cake[i] == '-')
		{
			count++;
			while (cake[++i] == '-');
		}
		for (; i < len; i++)
		{
			if (cake[i] == '-')
			{
				if (smile)
				{
					count += 2;
					smile = false;
				}
			}
			else
			{
				if (!smile)
					smile = true;
			}
		}
		printf("Case #%d: %d\n", t + 1, count);
	}
}