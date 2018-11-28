// Problem A. Pegman
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;
int R, C;
char m[110][110], v[110][110];

int check(int x, int y)
{
	int di = 0, dj = 0;
	for (int i = x, j = y; ; ) {
		if (v[i][j]) return 0;
		if (m[i][j] == '^') di = -1, dj = 0;
		else if (m[i][j] == 'v') di = 1, dj = 0;
		else if (m[i][j] == '<') di = 0, dj = -1;
		else if (m[i][j] == '>') di = 0, dj = 1;
		if (m[i][j] != '.') v[i][j] = 1;
		i += di; j += dj;
		if (i < 0 || i >= R || j < 0 || j >= C) return 1;
	}
	return 0;
}

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		int ans = -2;
		scanf("%d %d", &R, &C);
		for (int i = 0; i < R; i++) scanf("%s", m[i]);

		int ndots = 0;
		bool failed = false;
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++) {
				if (m[i][j] == '.') {
					ndots++;
					continue;
				}
				int n1 = 0, n2 = 0;
				for (int k = 0; k < R; k++) if (m[k][j] != '.') n1++;
				for (int k = 0; k < C; k++) if (m[i][k] != '.') n2++;
				if (n1 < 2 && n2 < 2) failed = true;
			}

		if (failed) ans = -1;
		if (ndots == R * C) ans = 0;

		if (ans < -1) {
			ans = 0;
			memset(v, 0, sizeof(v));
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					if (v[i][j] || m[i][j] == '.') continue;
					ans += check(i, j);
				}
			}
		}

		if (ans < 0)
			printf("Case #%d: IMPOSSIBLE\n", ti);
		else
			printf("Case #%d: %d\n", ti, ans);
	}

	return 0;
}
