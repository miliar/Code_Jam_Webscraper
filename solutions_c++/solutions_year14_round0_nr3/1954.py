#include <iostream>
#include <cstring>

using namespace std;

const int SZ = 16;
char grid[SZ][SZ];
int r, c, m;
int used = 0;
bool fnd;

const int dx[] = {-1,-1,-1,0,0,1,1,1};
const int dy[] = {-1, 0, 1,-1,1,-1,0,1};

bool BFS(const int sx, const int sy) {
	bool u[SZ][SZ] = {};
	u[sx][sy] = true;

	pair<int, int> q[SZ*SZ];
	q[0] = make_pair(sx, sy);
	int front = 1, rear = 0;

	while (front != rear) {
		const pair<int, int>& cur = q[rear++];
		//cerr << "fetching " << cur.first << ' ' << cur.second << endl;

		bool zero = true;

		for (int i=0; i<8; ++i) {
			const int nx = cur.first + dx[i];
			const int ny = cur.second + dy[i];

			if (nx >= 0 && ny >= 0 && nx < r && ny < c && grid[nx][ny] == '*') {
				zero = false;
				break;
			}
		}

		if (zero) {
			for (int i=0; i<8; ++i) {
				const int nx = cur.first + dx[i];
				const int ny = cur.second + dy[i];

				if (nx >= 0 && ny >= 0 && nx < r && ny < c && !u[nx][ny]) {
					u[nx][ny] = true;
					q[front++] = make_pair(nx, ny);
				}
			}
		}
	}

	for (int x=0; x<r; ++x) {
		for (int y=0; y<c; ++y) {
			if (!u[x][y] && grid[x][y] != '*')
				return false;
		}
	}

	return true;
}



void DFS(int x, int y) {
	if (y == c) {
		++x;
		y = 0;
	}

	if (x == r) {
		if (used == m) {
			for (int sx=0; sx<r; ++sx) {
				for (int sy=0; sy<c; ++sy) {
					if (grid[sx][sy] != '*') {
						if (BFS(sx, sy)) {
							grid[sx][sy] = 'c';
							fnd = true;
							for (int i=0; i<r; ++i)
								cout << grid[i] << endl;
							throw 5;
						}
					}
				}
			}
		}

		return;
	}

	++used;
	grid[x][y] = '*';
	DFS(x, y+1);
	--used;

	grid[x][y] = '.';
	DFS(x, y+1);
}

int main() {
	int t; cin >> t;

	for (int e=1; e<=t; ++e) {
		cin >> r >> c >> m;
		cout << "Case #" << e << ":" << endl;
		memset(grid, 0, sizeof grid);

		used = 0;
		fnd = false;
		try {
			DFS(0, 0);
		} catch (...) {}

		if (!fnd)
			cout << "Impossible" << endl;
	}

	return 0;
}


