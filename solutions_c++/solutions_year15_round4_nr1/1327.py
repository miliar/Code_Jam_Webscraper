#include <cstdio>
#include <cstring>

int T, R, C;
char grid[105][105];

int fr[105], lr[105], fc[105], lc[105];

int main() {
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t) {
		scanf("%d%d", &R, &C);
		memset(fr, -1, sizeof(fr));
		memset(fc, -1, sizeof(fc));
		memset(lr, -1, sizeof(lr));
		memset(lc, -1, sizeof(lc));
		for(int i = 0; i < R; ++i) {
			scanf("%s", grid[i]);
			for(int j = 0; grid[i][j]; ++j) {
				if(grid[i][j] != '.') {
					lc[j] = i;
					lr[i] = j;
					if(fr[i] == -1)
						fr[i] = j;
					if(fc[j] == -1)
						fc[j] = i;
				}
			}
		}
		int ct = 0;
		bool poss = true;
		for(int i = 0; i < R; ++i) {
			if(fr[i] == -1)
				continue;
			if(fr[i] == lr[i] && fc[fr[i]] == i && lc[fr[i]] == i) {
				poss = false;
				break;
			}
			if(grid[i][fr[i]] == '<')
				++ct;
			if(grid[i][lr[i]] == '>')
				++ct;
		}
		for(int i = 0; i < C; ++i) {
			if(fc[i] == -1)
				continue;
			if(fc[i] == lc[i] && fr[fc[i]] == i && lr[fc[i]] == i) {
				poss = false;
				break;
			}
			if(grid[fc[i]][i] == '^')
				++ct;
			if(grid[lc[i]][i] == 'v')
				++ct;
		}
		printf("Case #%d: ", t);
		if(!poss)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ct);
	}
	return 0;
}
