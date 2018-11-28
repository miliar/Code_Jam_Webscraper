#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int ca, n, m, tmp;
bool u[200][200], ans;
int a[200][200];

int main()
{
	freopen("b.out", "w", stdout);
	scanf("%d", &ca);
	for (int t = 1; t <= ca; t++) {
		scanf("%d%d", &n, &m);
		memset(u, 0, sizeof(u));
		for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);
		for (int i = 0; i < n; i++) {
			tmp = a[i][0];
			for (int j = 1; j < m; j++) tmp = max(a[i][j], tmp);
			for (int j = 0; j < m; j++) if (a[i][j] == tmp) u[i][j] = true;
		}
		for (int i = 0; i < m; i++) {
			tmp = a[0][i];
			for (int j = 1; j < n; j++) tmp = max(a[j][i], tmp);
			for (int j = 0; j < n; j++) if (a[j][i] == tmp) u[j][i] = true;
		}
		ans = true;
		for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (!u[i][j]) ans = false;
		printf("Case #%d: ", t);
		if (ans) printf("YES\n"); else printf("NO\n");
	}
	return 0;
}

