#include <stdio.h>
#include <iostream>

using namespace std;

int ans[21][21][21];

int main(int argc, char const *argv[]) {
	int t, x, r, c, tc = 0;
	cin >> t;
	for (int i = 1; i <= 4; ++i) {
		for (int j = 1; j <= 4; ++j) {
			ans[1][i][j] = 1;
			if (i * j % 2 == 0)
				ans[2][i][j] = 1;
		}
	}
	ans[3][2][3] = ans[3][3][2] = ans[3][3][3] = ans[3][3][4] = ans[3][4][3] = 1;
	ans[4][3][4] = ans[4][4][3] = ans[4][4][4] = 1;
	while (t--) {
		cin >> x >> r >> c;
		if (ans[x][r][c])
			printf("Case #%d: GABRIEL\n", ++tc);
		else
			printf("Case #%d: RICHARD\n", ++tc);
	}
	return 0;
}