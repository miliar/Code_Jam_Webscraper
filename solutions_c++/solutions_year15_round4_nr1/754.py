#include <cstdio>
#include <cstring>

using namespace std;

int edge[100][100][2];
int r, c;
char field[100][101];
int in[100][100];

int main(void) {
	int T;
	scanf("%d", &T);
	for(int kase = 1; kase <= T; kase++) {
		memset(edge, -1, sizeof(edge));
		memset(in, 0, sizeof(in));

		scanf("%d %d", &r, &c);
		for(int i = 0; i < r; i++) scanf("%s", field[i]);
		for(int i = 0; i < r; i++)
			for(int j = 0; j < c; j++) {
				if(field[i][j] == '.') continue;
				int dy, dx;
				if(field[i][j] == '>') dy = 0, dx = 1;
				if(field[i][j] == '^') dy = -1, dx = 0;
				if(field[i][j] == '<') dy = 0, dx = -1;
				if(field[i][j] == 'v') dy = 1, dx = 0;
				int y = i, x = j;
				while(y < r and x < c) {
					y += dy, x += dx;
					if(y >= r or y < 0 or x >= c or x < 0) {
						edge[i][j][0] = -2;
						break;
					} else if(field[y][x] != '.') {
						edge[i][j][0] = y;
						edge[i][j][1] = x;
						in[y][x]++;
						break;
					}
				}
			}

		int ans = 0;
		for(int i = 0; i < r and ans >= 0; i++)
			for(int j = 0; j < c and ans >= 0; j++)
				if(edge[i][j][0] == -2) {
					if(in[i][j] == 0) {
						bool isAble = false;
						for(int k = 0; k < r; k++) {
							if(k == i) continue;
							if(field[k][j] != '.') isAble = true;
						}
						for(int k = 0; k < c; k++) {
							if(k == j) continue;
							if(field[i][k] != '.') isAble = true;
						}
						if(isAble) ans++;
						else ans = -1;
					} else ans++;
				}

		printf("Case #%d: ", kase);
		if(ans == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}

	return 0;
}
