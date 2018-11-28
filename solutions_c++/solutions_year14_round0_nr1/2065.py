#include <cstdio>
#include <string.h>
#include <cstring>
int a[30][30], b[30][30], c[20];
int n, m, testnum;
int main() {
	freopen("A-small-attempt0.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testnum);
	for (int tt = 1; tt <= testnum; tt++) {
		scanf("%d", &n);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				scanf("%d", &a[i][j]);
		scanf("%d", &m);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				scanf("%d", &b[i][j]);
		memset(c, 0, sizeof(c));
		for (int i = 1; i <= 4; i++) { c[a[n][i]]+=1; c[b[m][i]] += 2; }
		int l = 0, k = 0;
		for (int i = 1; i <= 16; i++)
			if (c[i] == 3) { l++; k = i; }

		if (l == 0)
			printf("Case #%d: Volunteer cheated!\n", tt);
		if (l > 1)
			printf("Case #%d: Bad magician!\n", tt);
		if (l == 1)
			printf("Case #%d: %d\n", tt, k);

	}
	return 0;
}