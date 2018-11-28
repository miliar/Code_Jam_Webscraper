#include <cstdio>

int t, n, tmp, k, i, ti;

int main()
{
	scanf("%d", &t);
	for (ti = 1; ti <= t; ti++) {
		scanf("%d", &n);
		printf("Case #%d: ", ti);
		k = (n) ? 0:1023;
		for (i = 1; k != 1023; i++) {
			tmp = i*n;
			while (tmp) {
				k |= 1<<(tmp%10);
				tmp /= 10;
			}
		}
		if (n) printf("%d\n", (i-1)*n);
		else puts("INSOMNIA");
	}
	return 0;
}
