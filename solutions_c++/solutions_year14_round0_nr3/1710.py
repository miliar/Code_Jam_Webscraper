#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define debug(x) cout<<(#x)<<":"<<(x)<<endl

bool board[5][5], vis[5][5];
int r, c, nMine, clickX, clickY, area;
const int dx[8] = {0, -1, -1, -1, 0, 1, 1, 1};
const int dy[8] = {1, 1, 0, -1, -1, -1, 0, 1};

inline bool inside(int x, int y) {
	return 0<=x && x<r && 0<=y && y<c;
}

void floodfill(int x, int y) {
	vis[x][y] = 1;
	--area;
	bool zero = 1;
	REP(d, 8) {
		int nx = x + dx[d];
		int ny = y + dy[d];
		if (inside(nx, ny) && board[nx][ny]) {zero = 0; break;}
	}
	if (!zero) return;
	REP(d, 8) {
		int nx = x + dx[d];
		int ny = y + dy[d];
		if (inside(nx, ny) && !vis[nx][ny]) floodfill(nx, ny);
	}
}

bool pass() {
	for (clickX = 0; clickX < r; ++clickX)
	for (clickY = 0; clickY < c; ++clickY) if (!board[clickX][clickY]) {
		area = r*c - nMine;
		memcpy(vis, board, sizeof(board));
		floodfill(clickX, clickY);
		if (area == 0) return 1;
	}
	return 0;
}

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		printf("Case #%d:\n", cN);
		cin >> r >> c >> nMine;
		bool ok = 0;
		REP(b, (1<<(r*c))) {
			int cnt = 0;
			REP(x, r)
			REP(y, c) {
				bool isMine = b&(1<<(x*c+y));
				board[x][y] = isMine;
				cnt += isMine;
			}
			if (cnt != nMine) continue;
			if (pass()) {
				REP(x, r) {
					REP(y, c) {
						if (x == clickX && y == clickY) printf("c");
						else if (board[x][y]) printf("*");
						else printf(".");
					}
					puts("");
				}
				ok = 1;
				break;
			}
		}
		if (!ok) puts("Impossible");
	}
}
