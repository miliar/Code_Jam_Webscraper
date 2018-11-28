#include <iostream>
#include <algorithm>
#include <string>
#include <iomanip>
#include <vector>
using namespace std;

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, -1, 0, 1};

int r, c, match[1048576];
char field[256][256];
int init_x[256], init_y[256], init_d[256];

bool is_bounded(int x, int y) {
	return 0 <= x && x < r && 0 <= y && y < c;
}

bool build_path(int st, int ed) {
	int x = init_x[st], y = init_y[st], d = init_d[st];
	while (true) {
		// move forward one step
		x += dx[d]; y += dy[d];
		// if out of bound
		if (!is_bounded(x, y)) {
			d ^= 2; // turn around
			// if we have right destination
			if (x == init_x[ed] && y == init_y[ed] && d == init_d[ed]) {
				return true;
			} else {
				return false;
			}
		} else {
			if (field[x][y] == '/') {
				d ^= 1; // reflect along '/'
			} else if (field[x][y] == '\\') {
				d = 3 - d; // reflect along '\'
			} else {
				field[x][y] = (d % 2 == 0 ? '\\' : '/');
				d = (d + 3) % 4; // turn counterclockerwise
			}
		}
	}
}

bool build() {
	int gate_num = 2 * (r + c);
	vector<int> gates(gate_num);
	for (int i = 0; i < gate_num; i++)
		gates[i] = i;
	while ((int)gates.size() > 0) {
		int gate_num = (int)gates.size();

		bool match_found = false;
		// try to find a match
		for (int i = 0; i < gate_num; i++) {
			// if two neighborhoods match
			if (match[gates[i]] == gates[(i + 1) % gate_num]) {
				// try to build a path
				if (!build_path(gates[i], match[gates[i]])) {
					// if fails, report faliure
					return false;
				}
				// remove from gate list
				int e1 = i, e2 = (i + 1) % gate_num;
				gates.erase(gates.begin() + e1);
				gates.erase(gates.begin() + (e1 < e2 ? e2 - 1 : e2));

				match_found = true;
				break;
			}
		}

		if (!match_found)
			return false;
	}

	return true;
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		// initialize

		cin >> r >> c;
		// match
		for (int i = 0; i < 2 * (r + c); i += 2) {
			int a, b;
			cin >> a >> b;
			a--;
			b--;
			match[a] = b;
			match[b] = a;
		}
		// field
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++)
				field[i][j] = ' ';
			field[i][c] = '\0';
		}
		// init_x, init_y, init_d
		int cc = 0;
		for (int i = 0; i < c; i++) {
			init_x[cc] = -1; init_y[cc] = i; init_d[cc] = 0; cc++;
		}
		for (int i = 0; i < r; i++) {
			init_x[cc] = i; init_y[cc] = c; init_d[cc] = 1; cc++;
		}
		for (int i = c - 1; i >= 0; i--) {
			init_x[cc] = r; init_y[cc] = i; init_d[cc] = 2; cc++;
		}
		for (int i = r - 1; i >= 0; i--) {
			init_x[cc] = i; init_y[cc] = -1; init_d[cc] = 3; cc++;
		}

		// calculate
		bool ok = build();

		// print the answer
		cout << "Case #" << t << ":" << endl;
		if (ok) {
			// fill the field
			for (int i = 0; i < r; i++)
				for (int j = 0; j < c; j++)
					if (field[i][j] == ' ')
						field[i][j] = '/';
			for (int i = 0; i < r; i++)
				cout << field[i] << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
