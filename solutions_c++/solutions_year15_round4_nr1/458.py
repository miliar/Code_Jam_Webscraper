#include <bits/stdc++.h>
using namespace std;

ifstream fin("al0.in");
ofstream fout("a.out");
const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};
const char dir[] = {'>', 'v', '<', '^'};

int r,c;
char f[100][100]; // [r][c]

inline bool inb(int cr, int cc) {
	return (cr >= 0 && cr < r && cc >= 0 && cc < c);
}

string solve() {
	int res = 0;
	fin >> r >> c;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			fin >> f[i][j];
	for (int cr = 0; cr < r; cr++)
		for (int cc = 0; cc < c; cc++) {
			if (f[cr][cc] == '.') continue;

			bool gd = false;
			int ct = 0;
			for (int i = 0; i < 4; i++) {
				bool cok = false;
				int ccr = cr + dy[i], ccc = cc + dx[i];
				for (; inb(ccr, ccc); ccr += dy[i], ccc += dx[i])
					if (f[ccr][ccc] != '.') {
						cok = true;
						ct++;
						break;
					}
				if (cok && dir[i] == f[cr][cc]) gd = true;
			}
			if (gd) continue;
			if (ct == 0) return "IMPOSSIBLE";
			res++;
		}
	return to_string(res);
}

int main() {
	int a;
	fin >> a;
	for (int i = 0; i < a; i++) fout << "Case #" << i+1 << ": " << solve() << '\n';
}
