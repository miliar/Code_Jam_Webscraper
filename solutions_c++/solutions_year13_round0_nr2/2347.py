#include <stdio.h>
#include <algorithm>
using namespace std;

int T, m, n;
int h[100][100];
int r[100], c[100];

void work()
{
	static int ttt = 0;
	printf("Case #%d: ", ++ttt);
	scanf("%d%d\n", &m, &n);
	for (int i = 0; i < m; ++i) for (int j = 0; j < n; ++j) scanf("%d", &h[i][j]);
	for (int i = 0; i < m; ++i) {
		r[i] = 0;
		for (int j = 0; j < n; ++j) r[i] = max(r[i], h[i][j]);
	}
	for (int j = 0; j < n; ++j) {
		c[j] = 0;
		for (int i = 0; i < m; ++i) c[j] = max(c[j], h[i][j]);
	}
	bool ok = true;
	for (int i = 0; i < m; ++i) for (int j = 0; j < n; ++j) 
		if (h[i][j] != min(r[i], c[j])) ok = false;
	if (ok) printf("YES\n"); else printf("NO\n");
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d\n", &T);
	while (T--) work();
}