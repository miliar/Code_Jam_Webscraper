//author: whd

#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>
#include <set>
#include <map>

#define mp make_pair
#define pb push_back
#define x first
#define y second

using namespace std;
typedef long long big;

typedef pair<int, int> pii;

const int N = 222;
double a[N];
int n, m;
double f[N][N];
double b[N];
double calc() {
	int i, j;
	memset(f, 0, sizeof(f));
	f[0][0] = 1;
	for (i = 1; i <= m; i++) {
		for (j = 0; j <= m; j++) {
			f[i][j] += f[i - 1][j] * (1 - b[i]);
			if (j) {
				f[i][j] += f[i - 1][j - 1] * b[i];
			}
		}
	}
	return f[m][m / 2];
}
int main() {
	int cas, cass;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i, j, k;
	scanf("%d", &cas);
	for (cass = 1; cass <= cas; cass++) {
		printf("Case #%d:", cass);
		scanf("%d%d", &n, &m);
		for (i = 1; i <= n; i++)
			scanf("%lf", &a[i]);
		sort(a + 1, a + 1 + n);
		double ans = 0;
		for (i = 0; i <= m; i++) {
			k = 0;
			for (j = 1; j <= i; j++)
				b[++k] = a[j];
			for (j = n; k < m; j--)
				b[++k] = a[j];
			ans = max(ans, calc());
		}
		printf(" %.8f\n", ans);
	}
}
