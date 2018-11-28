#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

#define UP '^'
#define DOWN 'v'
#define RIGHT '>'
#define LEFT '<'

using namespace std;

bool in_board(int i, int j, int R, int C) {
	return ((i >= 0) && (j >= 0) && (i < R) && (j < C));
}

int main() {
	int t, T, R, C;
	cin >> T;
	for (t = 0; t < T; ++t) {
		cin >> R >> C;
		vector<string> b(R);
		for (int i = 0; i < R; ++i) {
			cin >> b[i];
		}

		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				if (b[i][j] != '.') {
					int dx[4] = {1, -1, 0, 0};
					int dy[4] = {0, 0, 1, -1};

					bool found = false;
					for (int k = 0; k < 4; ++k) {
						for (int m = 1; in_board(i+m*dx[k], j+m*dy[k], R, C); ++m) {
							if (b[i+m*dx[k]][j+m*dy[k]] != '.') {
								found = true;
							}
						}
					}

					if (!found) {
						cout << "Case #" << (t+1) << ": IMPOSSIBLE" << endl;
						goto end_loop;
					}
				}
			}
		}

		int total = 0;
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				if (b[i][j] == '.') {
					continue;
				}

				int dx = 0, dy = 0;
				if (b[i][j] == UP) {					
					dy = -1;
				} else if (b[i][j] == DOWN) {
					dy = 1;
				} else if (b[i][j] == LEFT) {
					dx = -1;
				} else {
					dx = 1;
				}

				bool found = false;
				for (int k = 1; in_board(i+k*dy, j+k*dx, R, C); ++k) {
					if (b[i+k*dy][j+k*dx] != '.') {
						found = true;
						break;
					}
				}

				if (!found) {
					total += 1;
				}
			}
		}
		
				
		cout << "Case #" << (t+1) << ": " << total << endl;

end_loop:
		;
	}
	return 0;
}