#include <stdio.h>
#include <stdlib.h>
int map[4][4];
const int X = 1, O = 0x10;
int testcase, caseno;

int judge(int count) {
	if ((count & 0xF) == X * 4) {
		printf("Case #%d: X won\n", caseno);
		return 1;
	}
	if ((count & 0xF0) == O * 4) {
		printf("Case #%d: O won\n", caseno);
		return 1;
	}
	return 0;
}
int main(){
#ifndef ONLINE_JUDGE
	freopen("E:\\A-small-attempt0.in", "r", stdin);
	freopen("E:\\test.out", "w", stdout);
#endif

	int i, j;
	int nx, no, nt, count;
	int solved = 0;
	char str[80];
	scanf("%d", &testcase);
	for (caseno = 1; caseno <= testcase; ++caseno) {
		nx = no = nt = 0;
		for (i = 0; i < 4; ++i) {
			scanf("%s", str);
			for (j = 0; j < 4; ++j) {
				if (str[j] == 'T') {
					map[i][j] = X + O;
					nt++;
				}
				else if (str[j] == 'X'){
					map[i][j] = X;
					nx++;
				}
				else if (str[j] == 'O'){
					map[i][j] = O;
					no++;
				}
				else map[i][j] = 0;
			}
		}
		count = 0;
		for (i = 0; i < 4; ++i) {
			count += map[i][i];
		}
		if (judge(count)) continue;
		count = 0;
		for (i = 0; i < 4; ++i) {
			count += map[i][3 - i];
		}
		if (judge(count)) continue;

		solved = 0;
		for (i = 0; i < 4; ++i) {
			count = 0;
			for (j = 0; j < 4; ++j) count += map[i][j];
			if (judge(count)) {
				solved = 1;
				break;
			}
		}
		if (solved) continue;

		solved = 0;
		for (j = 0; j < 4; ++j) {
			count = 0;
			for (i = 0; i < 4; ++i) count += map[i][j];
			if (judge(count)) {
				solved = 1;
				break;
			}
		}
		if (solved) continue;

		if (nt + nx + no == 16) printf("Case #%d: Draw\n", caseno);
		else printf("Case #%d: Game has not completed\n", caseno);
	}
	return 0;
}