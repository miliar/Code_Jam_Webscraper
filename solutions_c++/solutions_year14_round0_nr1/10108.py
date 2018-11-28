#include <cstdio>
#include <iostream>

using namespace std;

int main() {
	int T, m, n;
	int a[5][5], b[5][5];
	int i, j;
	scanf("%d", &T);
	int c = 1;
	while (T--) {
		scanf("%d", &m);
		for (i = 0; i < 4; i++)
		for (j = 0; j < 4; j++) {
			scanf("%d", &a[i][j]);
		}
		scanf("%d", &n);
		for (i = 0; i < 4; i++)
		for (j = 0; j < 4; j++) {
			scanf("%d", &b[i][j]);
		}
		int res = -1;
		int f1 = 0, f2 = 0;
		for (i = 0; i < 4; i++)
		for (j = 0; j < 4; j++) {
			if (f1) break;
			if (a[m-1][i] == b[n-1][j]) {
				if (res == -1) 
					res = a[m-1][i];
				else {
					f1 = 1;
					break;
				}
			}
		}
		if (res == -1) f2 = 1;
		printf("Case #%d: ", c++);
		if (f1) printf("Bad magician!\n");
		else if (f2) printf("Volunteer cheated!\n");
		else printf("%d\n", res);
	}
	return 0;
}