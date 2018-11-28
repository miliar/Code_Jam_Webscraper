#include <cstdio>

int solve(int n)
{
	if (n == 0) {
		return -1;
	}

	int sol = 0;

	int i;
	for (i = 1; sol < (1<<10) - 1; i++) {
		int c = n * i;
		while (c) {
			sol |= 1 << (c%10);
			c /= 10;
		}
	}
	--i;

	return i * n;
}

int main()
{
	int c;
	scanf("%d\n", &c);
	for (int i = 1; i <= c; i++) {
		int n;
		scanf("%d\n", &n);
		int sol = solve(n);
		if (sol < 0) {
			printf("Case #%d: INSOMNIA\n", i);
		} else {
			printf("Case #%d: %d\n", i, solve(n));
		}
	}
}
