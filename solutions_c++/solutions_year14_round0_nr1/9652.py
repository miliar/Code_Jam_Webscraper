#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
	int t = 0, T;
	scanf("%d", &T);
	for (t = 0; t < T; t ++) {
		int a, b;
		int x[4][4];
		int y[4][4];
		scanf("%d", &a);
		for (int i = 0; i < 4; i ++) {
			for (int j = 0; j < 4; j ++) {
				scanf("%d", &x[i][j]);
			}
		}
		scanf("%d", &b);
		for (int i = 0; i < 4; i ++) {
			for (int j = 0; j < 4; j ++) {
				scanf("%d", &y[i][j]);
			}
		}
		int ans = -1;
		a --, b --;
		for (int i = 0; i < 4; i ++) {
			for (int j = 0; j < 4; j ++) {
				if (x[a][i] == y[b][j]) {
					if (ans == -1) {
						ans = x[a][i];
					} else {
						ans = -2;
						printf("Case #%d: Bad magician!\n", t + 1);
						break;
					}
				}
			}
			if (ans == -2)
				break;
		}
		if (ans == -1) {
			printf("Case #%d: Volunteer cheated!\n", t + 1);
		} else if (ans > 0) {
			printf("Case #%d: %d\n", t + 1, ans);
		}
	}
}
