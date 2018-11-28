#include <cstdio>
#include <algorithm>

using namespace std;

int grid[123][123];
bool ok[123][123];
int h, w;

void hori(int row) {
	int cur = 0;
	for (int i=0; i<w; i++) {
		cur = max(cur, grid[row][i]);
	}
	for (int i=0; i<w; i++) {
		ok[row][i] |= (cur == grid[row][i]);
	}
}

void vert(int col) {
	int cur = 0;
	for (int i=0; i<h; i++) {
		cur = max(cur, grid[i][col]);
	}
	for (int i=0; i<h; i++) {
		ok[i][col] |= (cur == grid[i][col]);
	}
}

int main() {
	freopen("bigin.txt", "r", stdin);
	freopen("bigout.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ti=0; ti<t; ti++) {
		printf("Case #%d: ", ti+1);
		scanf("%d%d", &h, &w);
		for (int i=0; i<h; i++) {
			for (int j=0; j<w; j++) {
				scanf("%d", &grid[i][j]);
				ok[i][j] = false;
			}
		}
		for (int i=0; i<h; i++) {
			hori(i);
		}
		for (int i=0; i<w; i++) {
			vert(i);
		}
		bool isok = true;
		
		for (int i=0; i<h; i++) {
			for (int j=0; j<w; j++) {
				if (!ok[i][j]) isok = false;
			}
		}
		printf("%s\n", isok?"YES":"NO");
	}
	return 0;
}
