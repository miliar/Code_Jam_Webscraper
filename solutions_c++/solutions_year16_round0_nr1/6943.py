#include <cstdio>
#include <cstring>

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <=  T; ++t)
	{
		int c = 0, n;
		scanf("%d\n", &n);
		if (n == 0)
			printf("Case #%d: INSOMNIA\n", t);
		else
		for (int m = n; ; m += n)
		{
			for (int tmp = m; tmp; tmp /= 10)
			{
				c |= 1 << (tmp % 10);
				// fprintf(stderr, "%d\t", c);
			}
			if (c == 1023)
			{
				printf("Case #%d: %d\n", t, m);
				break;
			}
		}
	}

	return 0;
}
