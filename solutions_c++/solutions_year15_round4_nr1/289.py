#include <cstdio>

#define N 128
#define For(i, a, b) for (int i = (a); i < (b); ++i)
#define FoR(i, a, b) for (int i = (b - 1); i >= (a); --i)

int T, n, m, d[N][N], ans;
char s[N][N];
bool f;

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d%d", &n, &m);
		For(i, 0, n) scanf("%s", s[i]);
		For(i, 0, n) For(j, 0, m) d[i][j] = 0;
		f = 0;
		For(i, 0, n) {
			For(j, 0, m) if (s[i][j] != '.') {
				d[i][j] |= 1;
				break;
			}
			FoR(j, 0, m) if (s[i][j] != '.') {
				d[i][j] |= 2;
				break;
			}
		}
		For(j, 0, m) {
			For(i, 0, n) if (s[i][j] != '.') {
				d[i][j] |= 4;
				break;
			}
			FoR(i, 0, n) if (s[i][j] != '.') {
				d[i][j] |= 8;
				if (d[i][j] == 15) f = 1;
				break;
			}
		}
		if (f) {
			puts("IMPOSSIBLE");
			continue;
		}
		ans = 0;
		For(i, 0, n) For(j, 0, m) {
			if (s[i][j] == '<' && (d[i][j]&1)) ++ans;
			if (s[i][j] == '>' && (d[i][j]&2)) ++ans;
			if (s[i][j] == '^' && (d[i][j]&4)) ++ans;
			if (s[i][j] == 'v' && (d[i][j]&8)) ++ans;
		}
		printf("%d\n", ans);
	}
	return 0;
}
