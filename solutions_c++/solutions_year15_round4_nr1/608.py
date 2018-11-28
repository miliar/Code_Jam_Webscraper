#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> g;
const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};
int m, n;
int o;

int ch2di(char ch) {
	int d;
	if (ch == '>') d = 0;
	if (ch == 'v') d = 1;
	if (ch == '<') d = 2;
	if (ch == '^') d = 3;
	return d;
}

void gostr(int & x, int & y, int di) {
	x += dx[di];
	y += dy[di];	
	while (x >= 0 && x < m && y >= 0 && y < n && g[x][y] == '.') {
		x += dx[di];
		y += dy[di];
	}
	if (x >= 0 && x < m && y >= 0 && y < n) return;
	x = -1;
	y = -1;
}

int calc() {
	int res = 0;
	for (int i = 0; i < m; i ++) 
		for (int j = 0; j < n; j ++) {
			if (g[i][j] == '.') continue;
			int d = ch2di(g[i][j]);
			int x = i;
			int y = j;
			gostr(x, y, d);
			if (x < 0) {
				res ++;
				bool ok = false;
				for (int di = 0; di < 4; di ++) {
					if (di == d) continue;
					int x = i;
					int y = j;
					gostr(x, y, di);
					if (x >= 0 && y >= 0) {
						ok = true;
						break;
					}
				}
				if (!ok) {
					return -1;
				}
			}
		}
	return res;
}

int main() {
	int testcases;
	cin >> testcases;
	string line;
	for (int testcase = 0; testcase < testcases; testcase ++) {
		g.clear();
		cin >> m >> n;
		o = 0;
		g.resize(m);
		getline(cin, line);
		for (int i = 0; i < m; i ++) {
			getline(cin, line);
			g[i] = line;
		}
		o = calc();
		cout << "Case #" << testcase + 1 << ": ";
		if (o >= 0) cout << o; else cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}