#include <iostream>
using namespace std;

char map[110][110];
char flag[110][110];
int moved[110][110];

int main()
{
	int T, t;
	int R, C;
	int i, j, k;
	int ans;
	scanf("%d\n", &T);
	
	for (t = 1; t <= T; ++t) {
		ans = 0;
		scanf("%d %d\n", &R, &C);

		memset(map, 0, sizeof(map));
		memset(flag, 0, sizeof(flag));
		memset(moved, 0, sizeof(moved));

		for (i = 0; i < R; ++i) {
			for (j = 0; j < C; ++j) {
				scanf("%c\n", &map[i][j]);
				flag[i][j] = map[i][j];
			}
		}
		for (k = 0; k < 2; ++k) {
			for (i = 0; i < R; ++i) {
				// left to right
				for (j = 0; j < C; ++j) {
					if (map[i][j] == '.')
						continue;
					else {
						if (flag[i][j] == '<') {
							if (!moved[i][j]) {
								ans++;
								moved[i][j] = 1;
							}
							flag[i][j] = '>';
							if (map[i][j] == flag[i][j])
								goto impossible;
						}
						break;
					}
				}
				// right to left
				for (j = C - 1; j >= 0; --j) {
					if (map[i][j] == '.')
						continue;
					else {
						if (flag[i][j] == '>') {
							if (!moved[i][j]) {
								ans++;
								moved[i][j] = 1;
							}
							flag[i][j] = '^';
							if (map[i][j] == flag[i][j])
								goto impossible;
						}
						break;
					}
				}
			}

			for (j = 0; j < C; ++j) {
				// top to bottom
				for (i = 0; i < R; ++i) {
					if (map[i][j] == '.')
						continue;
					else {
						if (flag[i][j] == '^') {
							if (!moved[i][j]) {
								ans++;
								moved[i][j] = 1;
							}
							flag[i][j] = 'v';
							if (map[i][j] == flag[i][j])
								goto impossible;
						}
						break;
					}
				}
				// bottom to top
				for (i = R - 1; i >= 0; --i) {
					if (map[i][j] == '.')
						continue;
					else {
						if (flag[i][j] == 'v') {
							if (!moved[i][j]) {
								ans++;
								moved[i][j] = 1;
							}
							flag[i][j] = '<';
							if (map[i][j] == flag[i][j])
								goto impossible;
						}
						break;
					}
				}
			}
		}


		printf("Case #%d: %d\n", t, ans);
		continue;
impossible:
		printf("Case #%d: IMPOSSIBLE\n", t);
	}
}