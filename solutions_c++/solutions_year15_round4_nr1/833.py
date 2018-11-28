#include<cstdio>

int tt, r, c, g[105][105], ans;
char e;
bool im;

void init() {
	ans = 0;
	im = false;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &tt);
	for (int zzz = 1 ; zzz <= tt ; zzz++) {
		init();
		scanf("%d %d", &r, &c);
		for (int i = 0 ; i < r ; i++) {
			for (int j = 0 ; j < c ; j++) {
				scanf("%c", &e);
				if (e == '\n') scanf("%c", &e);
				switch (e) {
					case '^' : g[i][j] = 1; break;
					case '>' : g[i][j] = 2; break;
					case 'v' : g[i][j] = 3; break;
					case '<' : g[i][j] = 4; break;
					default : g[i][j] = 0; break;
				}
			}
		}
		for (int i = 0 ; i < r && !im ; i++) {
			for (int j = 0 ; j < c && !im ; j++) {
				int x = j, y = i;
				bool s = true, cbs = false;
				
				for (x = j, y = i - 1 ; y >= 0 ; y--) if (g[y][j]) break;
				if (y >= 0 && g[y][j]) cbs = true;
				else if (g[i][j] == 1) s = false;
//				printf("%d %d (^): stop at %d %d\n", i, j, y, x);
				
				for (x = j + 1, y = i ; x < c ; x++) if (g[i][x]) break;
				if (x < c && g[i][x]) cbs = true;
				else if (g[i][j] == 2) s = false;
//				printf("%d %d (>): stop at %d %d\n", i, j, y, x);
				
				for (x = j, y = i + 1 ; y < r ; y++) if (g[y][j]) break;
				if (y < r && g[y][j]) cbs = true;
				else if (g[i][j] == 3) s = false;
//				printf("%d %d (v): stop at %d %d\n", i, j, y, x);
				
				for (x = j - 1, y = i ; x >= 0 ; x--) if (g[i][x]) break;
				if (x >= 0 && g[i][x]) cbs = true;
				else if (g[i][j] == 4) s = false;
//				printf("%d %d (<): stop at %d %d\n", i, j, y, x);
				
				if (!s && cbs) ans++;
				else if (!s && !cbs) im = true;
			}
		}
		if (im) printf("Case #%d: IMPOSSIBLE\n", zzz);
		else printf("Case #%d: %d\n", zzz, ans);
	}
	scanf("\n");
	return 0;
}
