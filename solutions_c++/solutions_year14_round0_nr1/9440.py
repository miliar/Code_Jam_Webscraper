# include <stdio.h>

int mapper[1 << 17];
int a[5], b[5];

int main()
{
	// freopen("a.txt", "r", stdin);
	// freopen("b.txt", "w", stdout);

	int x, y, tc;

	scanf("%d", &tc);

	for (int i = 0; i < 16; i ++)
	{
		mapper[1 << i] = i + 1;
	}

	for (int p = 1; p <= tc; p ++)
	{
		printf("Case #%d: ", p);

		scanf("%d", &x);

		for (int i = 0; i < 4; i ++)
		{
			a[i] = 0;

			for (int j = 0; j < 4; j ++)
			{
				int t;

				scanf("%d", &t);

				a[i] |= (1 << (t - 1));
			}
		}

		scanf("%d", &y);

		for (int i = 0; i < 4; i ++)
		{
			b[i] = 0;

			for (int j = 0; j < 4; j ++)
			{
				int t;
				
				scanf("%d", &t);

				b[i] |= (1 << (t - 1));
			}
		}

		int ans = a[x - 1] & b[y - 1];

		// printf("%d %d %d\n", a[x], b[y]);

		if (ans == 0)
		{
			printf("Volunteer cheated!\n");
		} else
		if (ans & (ans - 1))
		{
			printf("Bad magician!\n");
		} else
		{
			printf("%d\n", mapper[ans]);
		}
	}
}