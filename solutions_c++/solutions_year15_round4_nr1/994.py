
#include <iostream>

using namespace std;

const int MAX = 200;

const char UP = '^';
const char DN = 'v';
const char LF = '<';
const char RT = '>';
const char NN = '.';

struct Input {
	int R, C;
	char cells[MAX][MAX];
};

struct Output {
	bool possible;
	int value;
};

bool hasfriend(int sr, int sc, int dr, int dc, Input in) {
	int r = sr + dr;
	int c = sc + dc;
	while (r >= 0 && c >= 0 && r < in.R && c < in.C) {
		if (in.cells[r][c] != NN) return true;
		r += dr;
		c += dc;
	}
	return false;
}

Output compute(Input in) {
	Output out;
	out.possible = true;
	out.value = 0;
	for (int r = 0; r < in.R; r++) {
		for (int c = 0; c < in.C; c++) {
			char cell = in.cells[r][c];
			int pdr = 0, pdc = 0;
			if (cell == NN) continue;
			if (cell == UP) {
				pdr = -1;
			} else if (cell == DN) {
				pdr = 1;
			} else if (cell == LF) {
				pdc = -1;
			} else if (cell == RT) {
				pdc = 1;
			}
			if (hasfriend(r, c, pdr, pdc, in)) continue;

			bool anyfriend = 
				((pdr != -1) && hasfriend(r, c, -1, 0, in)) ||
				((pdr != 1) && hasfriend(r, c, 1, 0, in)) ||
				((pdc != -1) && hasfriend(r, c, 0, -1, in)) ||
				((pdc != 1) && hasfriend(r, c, 0, 1, in));
			if (anyfriend) {
				out.value++;
			} else {
				out.possible = false;
				break;
			}
		}
		if (!out.possible) break;
	}
	return out;
}

ostream & operator << (ostream & out, const Output & output) {
	if (!output.possible) {
		return (out << "IMPOSSIBLE");
	} else {
		return (out << output.value);
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		Input in;
		cin >> in.R;
		cin >> in.C;
		string line;
		for (int r = 0; r < in.R; r++) {
			cin >> line;
			for (int c = 0; c < in.C; c++) {
				in.cells[r][c] = line[c];
			}
		}

		Output out = compute(in);
		cout << "Case #" << t << ": " << out << endl;
	}

	return 0;
}
