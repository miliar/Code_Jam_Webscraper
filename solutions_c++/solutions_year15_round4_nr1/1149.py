#include <string>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;



int ans = 0;
vector <string> mat;
vector <vector <int> > viz;
string dir = "<>v^";
bool solve_cell(int x, int y);


bool walk_from(int x, int y, char c) {
	if (c == '^') {
		--x;
	}
	else if (c == '>') {
		++y;
	}
	else if (c == '<') {
		--y;
	}
	else if (c == 'v') {
		++x;
	}
	if (0 <= x && 0 <= y && x < mat.size() && y < mat[0].size()) {
		if (mat[x][y] != '.') {
			if (solve_cell(x, y)) {
				return true;
			}
		}
		else {
			return walk_from(x, y, c);
		}
	}
	return false;
}

bool solve_cell(int x, int y) {
	if (viz[x][y] != 0) {
		return true;
	}
	viz[x][y] = 1;
	if (walk_from(x, y, mat[x][y])) {
		viz[x][y] = 2;
		return true;
	}
	for (auto c: dir) {
		if (walk_from(x, y, c)) {
			viz[x][y] = 2;
			++ans;
			return true;
		}
	}
	return false;
}

void solve() {
	int R, C, i, j;
	mat.clear();
	viz.clear();
	scanf("%d %d", &R, &C);
	ans = 0;
	viz.resize(R, vector <int> (C, 0));
	mat.resize(R);
	for (i = 0; i < R; ++i) {
		cin >> mat[i];
	}

	for (i = 0; i < R; ++i) {
		for (j = 0; j < C; ++j) {
			if (mat[i][j] != '.' && viz[i][j] == 0) {
				if (!solve_cell(i, j)) {
					cout << "IMPOSSIBLE\n";
					return;
				}
			}
		}
	}

	cout << ans << '\n';


}

int main(){

	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);

	int T, i;

	scanf("%d", &T);
	for (i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}

