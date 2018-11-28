#include <iostream>

using namespace std;

int t;
int r, c;

string s[111];
bool z[111][111];

int v;

void haku(int y, int x, int q) {
	if (y < 0 || y >= r || x < 0 || x >= c) {
		v++;
		return;
	}
	if (z[y][x]) return;
	if (s[y][x] == '.') {
		if (q == 1) haku(y-1,x,q);
		if (q == 2) haku(y,x+1,q);
		if (q == 3) haku(y+1,x,q);
		if (q == 4) haku(y,x-1,q);
	} else {
		z[y][x] = 1;
		if (s[y][x] == '^') haku(y-1,x,1);
		if (s[y][x] == '>') haku(y,x+1,2);
		if (s[y][x] == 'v') haku(y+1,x,3);
		if (s[y][x] == '<') haku(y,x-1,4);
	}
}

bool mahdoton() {
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (s[i][j] == '.') continue;
			int w = 0;
			for (int z = 0; z < r; z++) {
				if (s[z][j] != '.') w++;
			}
			for (int z = 0; z < c; z++) {
				if (s[i][z] != '.') w++;
			}
			if (w == 2) return true;
		}
	}
	return false;
}

void solve(int x) {
	cout << "Case #" << x << ": ";
	cin >> r >> c;
	for (int i = 0; i < r; i++) {
		cin >> s[i];
	}
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			z[i][j] = 0;
		}
	}
	if (mahdoton()) {
		cout << "IMPOSSIBLE\n";
		return;
	}
	v = 0;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (s[i][j] == '.') continue;
			if (z[i][j]) continue;
			haku(i,j,0);
		}
	}
	cout << v << "\n";
}

int main() {
	cin >> t;
	for (int x = 1; x <= t; x++) solve(x);
}
