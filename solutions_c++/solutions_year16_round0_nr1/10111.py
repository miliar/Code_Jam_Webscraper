#include <cstdio>

inline int digitnum(int a)
{
	int r=0;
	while (a) r++, a/=10;
	return r;
}

inline int digitsum(int a)
{
	int r=0;
	for (int i=0, j=digitnum(a); i<j; i++) {
		r |= 1 << (a % 10);
		a /= 10;
	}

	return r;
}

void exe(int c)
{
	int n, r=0;

	scanf("%d", &n);

	for (int i=1; i<=10000; i++) {
		r |= digitsum(n*i);
		if (r == ((1 << 10) - 1) ) {
			printf("Case #%d: %d\n", c, n*i);
			return;
		}
	}
	printf("Case #%d: INSOMNIA\n", c);
	return;
}

int main()
{
	freopen("in0.in", "r", stdin);
	freopen("out0.out", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int c=1; c<=t; c++) exe(c);
}
