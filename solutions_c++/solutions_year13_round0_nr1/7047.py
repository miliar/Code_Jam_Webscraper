#include <cstdio>
int testnum, x, o, t, d, px, py, ans;
char dat[8][8];
int check() {
	for (int i = 0;i < 4;i++) {
		bool suc = (dat[i][0] != '.');
		for (int j = 1;j < 4;j++) {
			if (dat[i][0] != dat[i][j])
				suc = false;
		}
		if (suc) return dat[i][0] == 'O' ? 1 : 0;
	}
	for (int i = 0;i < 4;i++) {
		bool suc = (dat[0][i] != '.');
		for (int j = 1;j < 4;j++) {
			if (dat[0][i] != dat[j][i])
				suc = false;
		}
		if (suc) return dat[0][i] == 'O' ? 1 : 0;
	}
	bool suc = (dat[0][0] != '.');
	for (int j = 1;j < 4;j++)
		if (dat[0][0] != dat[j][j])
			suc = false;
	if (suc) return dat[0][0] == 'O' ? 1 : 0;
	suc = (dat[0][3] != '.');
	for (int j = 1;j < 4;j++)
		if (dat[0][3] != dat[j][3 - j])
			suc = false;
	if (suc) return dat[0][3] == 'O' ? 1 : 0;
	if (d == 0) return 2;
	return 3;
}
int main() {
	scanf("%d", &testnum);
	for (int test = 1; test <= testnum; test++) {
		x = o = t = d = 0;
		for (int i = 0; i < 4; i++) {
			scanf("%s", dat[i]);
			for (int j = 0; j < 4; j++)
				if (dat[i][j] == 'X')
					x++;
				else if (dat[i][j] == 'O')
					o++;
				else if (dat[i][j] == 'T')
					t++;
				else
					d++;
		}
		ans = 3;
		if (t) {
			for (int i = 0;i < 4;i++) {
				for (int j = 0;j < 4;j++) {
					if (dat[i][j] == 'T') {
						px = i; py = j;
					}
				}
			}
			dat[px][py] = 'O';
			if ((ans = check()) > 1) {
				dat[px][py] = 'X';
				int tmp = check();
				ans = 3;
				if (tmp > 1) {
					if (d == 0)
						ans = 2;
				} else {
					ans = tmp;
				}
			}
		} else {
			ans = check();
		}
		printf("Case #%d: ", test);
		if (ans == 0)
			puts("X won");
		else if (ans == 1)
			puts("O won");
		else if (ans == 2)
			puts("Draw");
		else
			puts("Game has not completed");
	}
	return 0;
}
