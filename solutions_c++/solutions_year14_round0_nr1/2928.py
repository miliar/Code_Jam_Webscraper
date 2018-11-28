#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int N = 5;
int t, s1, s2, i, j;
int g1[N][N], g2[N][N], vis[20];

void solve() {
	int sum = 0;
	int v;
	for (int i = 1; i <= 16; i++) {
		if (vis[i]) sum ++;
		if (vis[i] == 2) v = i;
	}
	if (sum < 7) printf("Bad magician!\n");
	else if (sum > 7) printf("Volunteer cheated!\n");
	else printf("%d\n", v);
}

int main() {
	int cas = 0;
	scanf("%d", &t);
	while (t--) {	
		memset(vis, 0, sizeof(vis));
		scanf("%d", &s1);
		for (i = 0; i < 4; i ++)
			for (j = 0; j < 4; j++)
				scanf("%d", &g1[i][j]);
		scanf("%d", &s2);
		for (i = 0; i < 4; i ++)
			for (j = 0; j < 4; j++)
				scanf("%d", &g2[i][j]);
		for (i = 0; i < 4; i++)
			vis[g1[s1 - 1][i]]++;
		for (i = 0; i < 4; i++)
			vis[g2[s2 - 1][i]]++;
		printf("Case #%d: ", ++cas);
		solve();
	}
	return 0;
}