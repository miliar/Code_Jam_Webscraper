#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

pair<int, int> sim(int x, int y, int d, const vector<string> &v, int R, int C) {
	//cout << "sim " << x << ", " << y << ", " << d << " = ";
	int dx[2][4] = {
		{-1, 0, 1, 0},
		{1, 0, -1, 0}
	};
	int dy[2][4] = {
		{0, 1, 0, -1},
		{0, -1, 0, 1}
	};
	int dd[2][4] = {
		{1, 0, 3, 2},
		{3, 2, 1, 0}
	};
	while (true) {
		int m = (v[y][x]=='/' ? 0 : 1);
		int x2 = x + dx[m][d];
		int y2 = y + dy[m][d];
		int d2 = dd[m][d];
		x = x2;
		y = y2;
		d = d2;
		if (x < 0 || C <= x || y < 0 || R <= y) {
			//cout << "(" << x << ", " << y << ")" << endl;
			return make_pair(x, y);
		}
	}
}

void printv(const vector<string> &v) {
	for (auto &&s: v) {
		cout << s << endl;
	}
}

vector<string> solve(int R, int C, const vector<int> &lovers) {
	vector<string> v(R);
	vector<pair<int, int>> pos(2*(R+C));
	vector<int> dir(2*(R+C));
	int j = 0;
	for (int x = 0; x < C; x++, j++) {
		pos[j] = make_pair(x, 0);
		dir[j] = 0;
	}
	for (int y = 0; y < R; y++, j++) {
		pos[j] = make_pair(C-1, y);
		dir[j] = 1;
	}
	for (int x = C-1; x >= 0; x--, j++) {
		pos[j] = make_pair(x, R-1);
		dir[j] = 2;
	}
	for (int y = R-1; y >= 0; y--, j++) {
		pos[j] = make_pair(0, y);
		dir[j] = 3;
	}
	for (int i = 0; i < R; i++)
		v[i] = string(C, ' ');
	for (int i = 0; i < (1<<(R*C)); i++) {
		for (int y = 0; y < R; y++) {
			for (int x = 0; x < C; x++) {
				v[y][x] = ((i&(1<<(y*C+x))) ? '/' : '\\');
			}
		}
		//cout << "R=" << R << ", " << "C=" << C << endl;
		//printv(v);
		bool isok = true;
		for (int j = 0; j < 2*(R+C); j+=2) {
		    int k = lovers[j]-1;
			int rx, ry;
			tie(rx, ry) = sim(pos[k].first, pos[k].second, dir[k], v, R, C);
			int m;
			if (ry == -1) {
				m = rx+1;
			} else if (rx == C) {
				m = ry+1+C;
			} else if (ry == R) {
				m = (C-1-rx)+1+C+R;
			} else if (rx == -1) {
				m = (R-1-ry)+1+C*2+R;
			} else {
				cout << "error!" << endl;
				exit(1);
			}
			//cout << "m=" << m << ", " << lovers[j+1] << endl;
			if (m != lovers[j+1]) {
				isok = false;
				break;
			}
		}
		if (isok) {
			return v;
		}
	}
	return vector<string>();
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int R, C;
		cin >> R >> C;
		vector<int> lovers(2*(R+C));
		for (int i = 0; i < 2*(R+C); i+=2) {
			cin >> lovers[i] >> lovers[i+1];
		}
		vector<string> v = solve(R, C, lovers);
		cout << "Case #" << i+1 << ":" << endl;
		if (v.size() == 0) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			for (auto &&s: v) {
				cout << s << endl;
			}
		}
	}
}
