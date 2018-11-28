#include <cstdio>
#include <cstring>
using namespace std;
const int dx[4] ={-1, 0, 1, 0};
const int dy[4] ={0, 1, 0, -1};

int r, c;
char board[100][101];
bool visited[100][100];

int direction(char c) {
	if (c == '<') return 0;
	if (c == 'v') return 1;
	if (c == '>') return 2;
	return 3;
}

bool inBound(int y, int x) {
	return y >= 0 && y < r && x >= 0 && x < c;
}

bool isolated(int y, int x) {
	for (int d=0; d<4; ++d) {
		int ty = y + dy[d], tx = x + dx[d];
		bool flag = false;
		while (inBound(ty, tx)) {
			if (board[ty][tx] != '.') {
				flag = true;
				break;
			}
			ty += dy[d];
			tx += dx[d];
		}
		if (flag) return false;
	}
	return true;
}

int solve() {
	int ans = 0;
	for (int y=0; y<r; ++y)
		for (int x=0; x<c; ++x) {
			if (board[y][x] == '.' || visited[y][x]) continue;
			if (isolated(y, x)) return -1;
			int lx = x, ly = y, tx = x, ty = y;
			int d = 0;
			while (inBound(ty, tx) && !visited[ty][tx]) {
				if (board[ty][tx] != '.') {
					d = direction(board[ty][tx]);
					ly = ty;
					lx = tx;
					visited[ty][tx] = true;
				}
				ty += dy[d];
				tx += dx[d];
			}
			if (!inBound(ty, tx)) ++ans;
		}
	return ans;
}

int main() {
	freopen("r2\\A-large.in", "r", stdin);
	freopen("r2\\A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int N=1; N<=T; ++N) {
		scanf("%d%d", &r, &c);
		for (int y=0; y<r; ++y)
			scanf("%s", board+y);
		memset(visited, 0, sizeof visited);
		printf("Case #%d: ", N);
		int ans = solve();
		if (~ans)
			printf("%d\n", ans);
		else
			puts("IMPOSSIBLE");
	}
}