#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;

char str[16][3][(1 << 12) + 5];
int dir[3][2] = {{0, 2}, {1, 0}, {2, 1}};
int kP[16][3], kR[16][3], kS[16][3];
char ans[(1 << 12) + 5];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);

	strcpy(str[0][0], "R");
	strcpy(str[0][1], "P");
	strcpy(str[0][2], "S");
	for (int i = 1; i <= 12; ++i) {
		for (int d = 0; d < 3; ++d) {
			int d1 = dir[d][0], d2 = dir[d][1];
			if (strcmp(str[i - 1][d1], str[i - 1][d2]) < 0) {
				int l = strlen(str[i - 1][d1]);
				for (int j = 0; j < l; ++j) {
					str[i][d][j] = str[i - 1][d1][j];
				}
				for (int j = 0; j < l; ++j) {
					str[i][d][j + l] = str[i - 1][d2][j];
				}
				str[i][d][2 * l] = 0;
			} else {
				int l = strlen(str[i - 1][d1]);
				for (int j = 0; j < l; ++j) {
					str[i][d][j] = str[i - 1][d2][j];
				}
				for (int j = 0; j < l; ++j) {
					str[i][d][j + l] = str[i - 1][d1][j];
				}
				str[i][d][2 * l] = 0;
			}
			int l = strlen(str[i][d]);
			kP[i][d] = 0;
			kR[i][d] = 0;
			kS[i][d] = 0;
			for (int j = 0; j < l; ++j) {
				if (str[i][d][j] == 'P') kP[i][d]++;
				if (str[i][d][j] == 'S') kS[i][d]++;
				if (str[i][d][j] == 'R') kR[i][d]++;
			}
		}
	}

	int _, cas = 1;
	scanf("%d", &_);
	while (_--) {
		printf("Case #%d: ", cas);
		++cas;
		
		int n, R, P, S;
		scanf("%d%d%d%d", &n, &R, &P, &S);
		int len = (1 << n);
		for (int i = 0; i < len; ++i) ans[i] = 'Z';
		for (int d = 0; d < 3; ++d) {
			if (kP[n][d] == P && kR[n][d] == R && kS[n][d] == S) {
				if (strcmp(ans, str[n][d]) > 0) {
					for (int j = 0; j < len; ++j) {
						ans[j] = str[n][d][j];
					}
					ans[len] = 0;
				}
			}
		}
		if (ans[0] == 'Z') {
			puts("IMPOSSIBLE");
		} else {
			puts(ans);
		}
	}
 	return 0;
}