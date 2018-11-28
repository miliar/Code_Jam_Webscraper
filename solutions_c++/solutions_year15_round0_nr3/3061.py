#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
const int b[][4] = {
	{0, 0, 0, 0},
	{0, 1, 0, 1},
	{0, 1, 1, 0},
	{0, 0, 1, 1}
};
const int c[][4] = {
	{0, 1, 2, 3},
	{1, 0, 3, 2},
	{2, 3, 0, 1},
	{3, 2, 1, 0}
};
int test, n, m, a[1111], z[300];
char st[11111111];
long long L;

long long find(long long s, int r)
{
	int x = 0, y = 0;
	for (int i = 0; s + i <= L && i <= 4 * n; i ++) {
		int k = z[st[(s + i) % n]];
		x ^= b[y][k];
		y = c[y][k];
		if (x == 0 && y == r) return s + i + 1;
	}
	return L + 1;
}

int main()
{
	z['i'] = 1;
	z['j'] = 2;
	z['k'] = 3;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d", &test);
	int ncase = 0;
	while (test --) {
		scanf("%d%d", &n, &m);
		L = (long long)n * m;
		scanf("%s", st);
		printf("Case #%d: ", ++ncase);
		int x = 0, y = 0;
		for (int i = 0; i < n; i ++) {
			x ^= b[y][z[st[i]]];
			y = c[y][z[st[i]]];
		}
		long long S = find(find(0LL, 1), 2);
	//	printf("%lld\n", S);
		if (S >= L) {
			printf("NO\n");
			continue;
		}
		int xx = 0, yy = 0;
		while (S % n != 0) {
			int k = z[st[S % n]];
			xx ^= b[yy][k];
			yy = c[yy][k];
			S ++;
		}
		int mm = (L - S) / n;
		mm %= 4;
		xx = (xx + mm * x) % 2;
		for (int i = 0; i < mm; i ++) {
			xx ^= b[yy][y];
			yy = c[yy][y];
		}
		if (xx == 0 && yy == 3) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}
	return 0;
}

