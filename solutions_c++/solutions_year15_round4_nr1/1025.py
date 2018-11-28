#include <iostream>
#include <unordered_map>

using namespace std;

const int N = 104;

char grid[N][N];

unordered_map<int, int> table;

int dir[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

bool saveWalk(int dirIdx, int posY, int posX, int h, int w) {
	bool flag = false;
	for (int i = posY+dir[dirIdx][0], j = posX+dir[dirIdx][1]; 0 <= i && i < h && 0 <= j && j < w; i += dir[dirIdx][0], j+= dir[dirIdx][1]) {
		if (grid[i][j] != '.') {
			flag = true; 
			break;
		}
	}
	return flag;
}

int isSave(int curDir, int posY, int posX, int h, int w) {
	int flag = -1;
	if (saveWalk(curDir, posY, posX, h, w) == true) return 0;
	for (int dirIdx = 0; dirIdx < 4; dirIdx++) {
		if (curDir == dirIdx) continue;
		if (saveWalk(dirIdx, posY, posX, h, w) == true) return 1;
	}
	return flag;
}

int getDirFromChar(char ch) {
	if (ch == '^') return 0;
	if (ch == '<') return 1;
	if (ch == 'v') return 2;
	if (ch == '>') return 3;
	return -1;

}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		table.clear();
		int h, w;
		scanf("%d%d", &h, &w);
		for (int i = 0; i < h; i++) {
			scanf("%s", grid[i]);
		}
		for (int j = 0; j < w; j++) {
			for (int i = 0; i < h; i++) {
				if (grid[i][j] != '.' && table.find(i*w+j) == table.end()) {
					table[i*w+j] = getDirFromChar(grid[i][j]);
					break;
				}
			}
		}
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (grid[i][j] != '.' && table.find(i*w+j) == table.end()) {
					table[i*w+j] = getDirFromChar(grid[i][j]);
					break;
				}
			}
		}
		for (int j = 0; j < w; j++) {
			for (int i = h-1; i >= 0; i--) {
				if (grid[i][j] != '.' && table.find(i*w+j) == table.end()) {
					table[i*w+j] = getDirFromChar(grid[i][j]);
					break;
				}
			}
		}
		for (int i = 0; i < h; i++) {
			for (int j = w-1; j >= 0; j--) {
				if (grid[i][j] != '.' && table.find(i*w+j) == table.end()) {
					table[i*w+j] = getDirFromChar(grid[i][j]);
					break;
				}
			}
		}

		int ans = 0;
		for (unordered_map<int, int>::iterator iter = table.begin(); iter != table.end(); iter++) {
			int pos = iter->first;
			int dirIdx = iter->second;
			int cnt = isSave(dirIdx, pos/w, pos%w, h, w);
			if (cnt == -1) {
				ans = -1;
				break;
			}
			else {
				ans += cnt;
			}
		}
		if (ans == -1) {
			printf("Case #%d: IMPOSSIBLE\n", cas);
		}
		else {
			printf("Case #%d: %d\n", cas, ans);
		}
	}
	return 0;
}