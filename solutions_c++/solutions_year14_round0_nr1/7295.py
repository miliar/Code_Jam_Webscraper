#include <cstdio>
#include <cstdlib>

int main() {
	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; ++ cas) {
		int a[5][5], b[5][5], n, m;
		scanf("%d", &n); n --;
		for (int i = 0; i < 4; ++ i) 
			for (int j = 0; j < 4; ++ j) {
				scanf("%d", &a[i][j]);
			}
		scanf("%d", &m); m --;
		for (int i = 0; i < 4; ++ i) 
			for (int j = 0; j < 4; ++ j) {
				scanf("%d", &b[i][j]);
			}
		int cnt = 0, w;
		for (int i = 0; i < 4; ++ i)
			for (int j = 0; j < 4; ++ j)
				if (a[n][i] == b[m][j]) {
					cnt ++;
					w = a[n][i];
				}
		printf("Case #%d: ", cas);
		if (cnt == 1) printf("%d\n", w);
		else if (cnt != 0) puts("Bad magician!");
		else puts("Volunteer cheated!");
	}
	return 0;
}
