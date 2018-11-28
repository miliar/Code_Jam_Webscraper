#include <stdio.h>

#define N 205

int n, k;
double a[N], d[N][N], b[N];
double ans;

double get_d(int j, int l)
{
	if (j<0 || l < 0) return 0;
	return d[j][l];
}

void calc()
{
	for (int i = 0; i <=k; i++) {
		for (int j = 0; j <= k; j++) d[i][j] = 0;
	}

	d[0][0] = 1;
	for (int i = 1; i <= k; i++) {
		for (int j = 0; j <= i; j++) {
			d[i][j] = get_d(i-1,j-1)*b[i] + get_d(i-1,j)*(1 - b[i]);
		}
	}
	if (ans < d[k][k / 2]) ans = d[k][k / 2];
}

void func(int lev, int i)
{
	if (lev > k) {
		calc();
		return;
	}

	for (; i <= n; i++) {
		b[lev] = a[i];
		func(lev + 1, i + 1);
	}
}

void process()
{
	scanf("%d %d", &n, &k);
	ans = 0;
	for (int i = 1; i <= n; i++) scanf("%lf", &a[i]);

	func(1,1);

	printf("%.7lf\n", ans);
}

int main()
{
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		process();
	}
	return 0;
}