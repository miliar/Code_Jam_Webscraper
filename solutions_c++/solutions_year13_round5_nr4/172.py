#include <stdio.h>
#include <iostream>
#define two(x) (1 << (x))

const int N = 20;
double f[two(N)];
char s[25];

int init_s;
int n;

void work()
{
	gets(s);
	init_s = 0;
	n = strlen(s);
	for (int i = 0; i < n; ++i) if (s[i] == 'X')
		init_s = init_s + two(i);
	memset(f, 0, sizeof(f));
	for (int msk = two(n) - 2; msk >= 0; --msk) {
		if ((msk & init_s) != init_s) continue;
		for (int i = 0; i < n; ++i) {
			int j = 0;
			while ((msk & two((i + j) % n)) != 0) ++j;
			int msk2 = msk | two((i + j) % n);
			f[msk] += (f[msk2] + n - j) / n;
		}
	}
	static int ttt = 0;
	printf("Case #%d: %.10f\n", ++ttt, f[init_s]);
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int T;
	scanf("%d\n", &T);
	while (T--) work();
}