#include <bits/stdc++.h>

using namespace std;

const int M = 120;

int r, c;
char a[M][M], b[M][M], ar[M][M], br[M][M];

void read() {
	cin >> r >> c;
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j) {
			cin >> a[i][j];
			b[j][i] = a[i][j];
			ar[i][c - 1 - j] = a[i][j];
			br[j][r - 1 - i] = b[j][i];
		}
}

// order: > ^ < v

int getDir(char c) {
	switch (c) {
		case '>' : return 0;
		case '^' : return 1;
		case '<' : return 2;
		case 'v' : return 3;
	}
}

vector<string> chunk(int i, int j) {
	return vector<string>({
		string(a[i] + j + 1, a[i] + c),
		string(b[j], b[j] + i),
		string(a[i], a[i] + j),
		string(b[j] + i + 1, b[j] + r)
	});	
}

bool hasDir(string s) {
	for (char c : s)
		if (c == '<' || c == '>' || c == 'v' || c == '^')
			return true;
	return false;
}

void kill() {
	int ans = 0;
	bool pos = true;
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j) {
			auto dirs = chunk(i, j);
			if (a[i][j] == '.')
				continue;
			int d = getDir(a[i][j]);
			if (hasDir(dirs[d]))
				continue;
			bool found = false;
			for (auto dr : dirs)
				if (hasDir(dr)) {
					++ans;
					found = true;
					break;
				}
			if (!found)
				pos = false;
		}
	if (pos) {
		cout << ans << "\n";
	} else {
		cout << "IMPOSSIBLE\n";
	}
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		read();
		cout << "Case #" << i << ": ";
		kill();
	}
}