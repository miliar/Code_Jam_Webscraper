#include <iostream>
#include <fstream>
#include <set>
using namespace std;

ifstream inf("A-large.in");
ofstream ouf("output.txt");

void solve() {
	int R, C; inf >> R >> C;
	char grid[100][100];
	for (int r = 0; r < R; ++r) {
		for (int c = 0; c < C; ++c) {
			inf >> grid[r][c];
		}
	}
	int dir[4][2] = {
		{ -1, 0 },
		{ 0, 1 },
		{ 1, 0 },
		{ 0, -1 }
	};
	char ch[4] = { '^', '>', 'v', '<' };
 	int answer = 0;
	for (int r = 0; r < R; ++r) {
		for (int c = 0; c < C; ++c) {
			if (grid[r][c] == '.') continue;
			set<char> safe;
			for (int d = 0; d < 4; ++d) {
				int x = c, y = r;
				while (true) {
					int x_ = x + dir[d][1], y_ = y + dir[d][0];
					if (x_ < 0 || y_ < 0 || x_ >= C || y_ >= R) break;
					else {
						x = x_;
						y = y_;
					}
					if (grid[y][x] != '.') {
						safe.insert(ch[d]);
						break;
					}
				}
			}
			if (safe.size() == 0) {
				ouf << "IMPOSSIBLE";
				return;
			}
			if (safe.find(grid[r][c]) == safe.end()) {
				answer++;
			}
		}
	}
	ouf << answer;
}

int main() {
	int T; inf >> T;
	for(int t = 1; t <= T; ++t) {
		ouf << "Case #" << t << ": ";
		solve();
		ouf << "\n";
	}
	return 0;
}