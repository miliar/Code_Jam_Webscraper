#include <cstdio>

const int MAX = 110;

int w, h;
char map[MAX][MAX];
bool out[MAX][MAX], change[MAX][MAX];

void updateX(int y, int x, char target, int &last) {
	if(map[y][x] != '.') {
		if(last == -1) {
			if(map[y][x] == target)
				out[y][x] = 1;
			last = x;
		} else {
			change[y][last] = 1;
			last = x;
		}
	}
}

void updateY(int y, int x, char target, int &last) {
	if(map[y][x] != '.') {
		if(last == -1) {
			if(map[y][x] == target)
				out[y][x] = 1;
			last = y;
		} else {
			change[last][x] = 1;
			last = y;
		}
	}
}

int main() {
	freopen("A.out", "w", stdout);

	int numCase, nowCase;
	scanf("%d", &numCase);

	for(nowCase = 1; nowCase <= numCase; nowCase++) {
		scanf("%d%d", &h, &w);

		int i, j;
		for(i = 1; i <= h; i++)
			scanf("%s", map[i]+1);
		
		int last;
		for(i = 1; i <= h; i++) {
			for(j = 1; j <= w; j++) {
				out[i][j] = 0;
				change[i][j] = 0;
			}

			last = -1;
			for(j = 1; j <= w; j++) {
				updateX(i, j, '<', last);
			}

			last = -1;
			for(j = w; j >= 1; j--) {
				updateX(i, j, '>', last);
			}
		}

		for(j = 1; j <= w; j++) {
			last = -1;
			for(i = 1; i <= h; i++) {
				updateY(i, j, '^', last);
			}
			
			last = -1;
			for(i = h; i >= 1; i--) {
				updateY(i, j, 'v', last);
			}
		}

		int ans = 0;
		for(i = 1; i <= h; i++) {
			for(j = 1; j <= w; j++) {
				if(out[i][j] == 1) {
					if(change[i][j]) ans++;
					else {
						printf("Case #%d: IMPOSSIBLE\n", nowCase);
						goto caseEnd;
					}
				}
			}
		}

		printf("Case #%d: %d\n", nowCase, ans);

	caseEnd:;
	}

	return 0;
}