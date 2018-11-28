#include <cstdio>

using namespace std;

int main() {
	char buf[500];
	int T;
	int i;

	char maps[102][102];
	int j, k;

	fgets(buf, 500, stdin);

	sscanf(buf, "%d", &T);

	for (i = 0; i < T; ++i) {
		fgets(buf, 500, stdin);

		int R, C;

		sscanf(buf, "%d %d", &R, &C);

		for (j = 0; j < R; ++j) {
			fgets(maps[j], 102, stdin);
		}

		int res = 0;

		for (j = 0; j < R; ++j) {
			for (k = 0; k < C; ++k) {

				if (maps[j][k] == '.')
					continue;

				int a, b;
				bool a1 = false;
				bool a2 = false;
				bool b1 = false;
				bool b2 = false;

				for (a = 0; a < j; ++a) {
					if (maps[a][k] != '.') {
						a1 = true;
						break;
					}
				}
				for (a = j + 1; a < R; ++a) {
					if (maps[a][k] != '.') {
						a2 = true;
						break;
					}
				}

				for (b = 0; b < k; ++b) {
					if (maps[j][b] != '.') {
						b1 = true;
						break;
					}
				}
				for (b = k + 1; b < C; ++b) {
					if (maps[j][b] != '.') {
						b2 = true;
						break;
					}
				}

				if (!a1 && !a2 && !b1 && !b2) {
					res = -1;
					break;
				}

				if (a1 && maps[j][k] == '^')
					continue;
				if (a2 && maps[j][k] == 'v')
					continue;
				if (b1 && maps[j][k] == '<')
					continue;
				if (b2 && maps[j][k] == '>')
					continue;

				++res;
			}

			if (res == -1)
				break;
		}

		if (res == -1)
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		else
			printf("Case #%d: %d\n", i + 1, res);
	}
}