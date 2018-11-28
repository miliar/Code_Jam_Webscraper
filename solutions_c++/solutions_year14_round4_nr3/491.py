#include <iostream>
#include <cassert>
#include <cstring>

using namespace std;

int W, H;
char bord[600][600];
bool visited[600][600];

int di[] = {1, 0, -1, 0};
int dj[] = {0, 1, 0, -1};

bool dfs(int i, int j, int dir) {
	if (i < 0 || i >= H || j < 0 || j >= W) return false;
	if (bord[i][j] == 'x') return false;
	if (visited[i][j]) return false;
	visited[i][j] = true;
	if (i == H - 1) {
		bord[i][j] = 'x';
		return true;
	}
	for (int d = 0; d < 4; d++) {
		int e = (d + dir + 3) % 4;
		if (dfs(i + di[e], j + dj[e], e)) {
			bord[i][j] = 'x';
			return true;
		}
	}
	return false;
}

bool doeDfs() {
	memset(visited, 0, sizeof visited);
	for (int i = 0; i < W; i++) {
		if (dfs(0, i, 0)) return true;
	}
	return false;
}

void printBord() {
	/*for (int i = 0; i < H; i++)
		cerr << bord[i] << endl;
	cerr << endl;*/
}

int solve() {
	int B;
	cin >> W >> H >> B;
	assert(W >= 3 && W <= 100);
	assert(H >= 3 && H <= 500);
	assert(B >= 0 && B <= 10);
	memset(bord, '.', sizeof bord);
	for (int i = 0; i < H; i++)
		bord[i][W] = '\0';
	for (int i = 0; i < B; i++) {
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		for (int y = b; y <= d; y++) {
			for (int x = a; x <= c; x++) {
				bord[y][x] = 'x';
			}
		}
	}
	printBord();
	int tel = 0;
	while (doeDfs()) {
		tel++;
		printBord();
	}
	return tel;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": " << solve() << endl;
	}
	return 0;
}
