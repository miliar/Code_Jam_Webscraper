#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int n, r, c;
int layout[101][101];

ifstream fin("A-large.in");
ofstream fout("test.out");

int d[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

int get_d_num(char ch) {
	switch(ch) {
		case '^':
			return 2;
		case 'v':
			return 0;
		case '<':
			return 3;
		case '>':
			return 1;
	}
	return -1;
}

bool on_edge(int x, int y) {
	return x >= 1 && x <= r && y >= 1 && y <= c;
}

int main() {
	int t;
	fin >> t;
	for (int case_num = 1; case_num <= t; case_num++) {
		fin >> r >> c;
		for (int i = 1; i <= r; i++) {
			string line;
			fin >> line;
			for (int j = 1; j <= c; j++)
				layout[i][j] = line[j - 1];
		}
		int res = 0;
		bool gflag = true;
		for (int i = 1; i <= r; i++) {
			for (int j = 1; j <= c; j++) {
				if (layout[i][j] == '.')
					continue;
				int d_num = get_d_num(layout[i][j]);
				int x = i + d[d_num][0], y = j + d[d_num][1];
				while (on_edge(x, y)) {
					if (layout[x][y] != '.')
						break;
					x += d[d_num][0];
					y += d[d_num][1];
				}
				if (on_edge(x, y))
					continue;
				bool flag = false;
				for (int k = 0; k < 4; k++)
					if (k != d_num) {
						x = i + d[k][0];
						y = j + d[k][1];
						while (on_edge(x, y)) {
							if (layout[x][y] != '.')
								break;
							x += d[k][0];
							y += d[k][1];
						}
						if (on_edge(x, y)) {
							flag = true;
							break;
						}
					}
				if (!flag) {
					gflag = false;
					break;
				}
				res++;
			}
			if (!gflag)
				break;
		}
		fout << "Case #" << case_num << ": ";
		if (gflag)
			fout << res;
		else
			fout << "IMPOSSIBLE";
		fout << endl;
	}
	return 0;
}