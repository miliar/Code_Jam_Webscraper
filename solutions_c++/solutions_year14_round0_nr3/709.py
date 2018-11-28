#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

// Problem C. Minesweeper Master

//string infile = "sample.txt";
//string infile = "C-small-attempt0.in";
string infile = "C-large.in";
string outfile = "output.txt";

ifstream in(infile);
ofstream out(outfile);

struct Field {
	vector<vector<int>> f;
	int R;
	int C;
	int cleared;
	
	Field () {}

	Field (int rows, int columns) {
		R = rows;
		C = columns;
		f = vector<vector<int>>(R, vector<int>(C, 2));
		cleared = 0;
	}

	string to_string () {
		string s = "";
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				s += ((f[i][j] == -1) ? 'c' : (f[i][j] < 2) ? '.' : '*');
			}
			s += "\n";
		}
		return s;
	}

	void update (int x, int y) {
		for (int i = -1; i <= 1; ++i) {
			for (int j = -1; j <= 1; ++j) {
				int a = x + i;
				int b = y + j;
				if ((a >= 0) && (a < R) && (b >= 0) && (b < C)) {
					if (f[x+i][y+j] > 1) {
						f[x+i][y+j] = 1;
						++cleared;
					}
				}
			}
		}
	}

	void click (int x, int y, int value) {
		if (f[x][y] == 2) {
			++cleared;
		}
		f[x][y] = value;
		update(x, y);
	}
};

unordered_set<string> seen;

bool sweep(const Field& F, int stop, int x, int y, int value = 0) {
	Field NF = F;
	NF.click(x, y, value);
	if (seen.find(NF.to_string()) != seen.end()) {
		return false;
	} else {
		seen.insert(NF.to_string());
	}
	if (NF.cleared == stop) {
		out << NF.to_string();
		return true;
	} else if (NF.cleared > stop) {
		return false;
	}
	for (int i = 0; i < NF.R; ++i) {
		for (int j = 0; j < NF.C; ++j) {
			if (NF.f[i][j] == 1) {
				if(sweep(NF, stop, i, j)) {
					return true;
				}
			}
		}
	}
	return false;
}

void start_sweep (int R, int C, int M) {
	Field F(R, C);
	int stop = R*C - M;
	for (int i = 0; i < ceil(R/2.0); ++i) {
		for (int j = 0; j < ceil(C/2.0); ++j) {
			seen.clear();
			if (sweep(F, stop, i, j, -1)) {
				return;
			}
		}
	}
	out << "Impossible" << endl;
}

int main () {

	int T;
	in >> T;
	for (int i = 1; i <= T; ++i) {
		int R;	// number of rows
		int C;	// number of columns
		int M;	// number of mines
		in >> R >> C >> M;
		out << "Case #" << i << ":" << endl;
		if (M == 0) {
			out << 'c' << string(C - 1, '.') << endl;
			for (int i = 1; i < R; ++i) {
				out << string(C, '.') << endl;
			}
		} else if (R*C - 1 == M) {
			out << 'c' << string(C - 1, '*') << endl;
			for (int i = 1; i < R; ++i) {
				out << string(C, '*') << endl;
			}
		} else {
			start_sweep(R, C, M);
		}
	}

	return 0;
}
