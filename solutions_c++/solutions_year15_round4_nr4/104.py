#include <iostream>
#include <unordered_set>

using namespace std;

int t;
int r, c;
unordered_set<string> q;

int s[30][30];
int cc;

bool ok(int y, int x) {
	int z = 0;
	if (s[y-1][x] == s[y][x]) z++;
	if (s[y+1][x] == s[y][x]) z++;
	if (x > 1 && s[y][x-1] == s[y][x]) z++;
	if (x == 1 && s[y][c] == s[y][x]) z++;
	if (x < c && s[y][x+1] == s[y][x]) z++;
	if (x == c && s[y][1] == s[y][x]) z++;
	return z == s[y][x];
}

bool alku(int y) {
	for (int i = 1; i < y; i++) {
		for (int j = 1; j <= c; j++) {
			if (!ok(i,j)) return false;
		}
	}
	return true;
}

void valmis() {
	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			if (!ok(i,j)) return;
		}
	}
	string hh;
	for (int z = 0; z < c; z++) {
		hh = "";
		for (int i = 1; i <= r; i++) {
			for (int j = 1; j <= r; j++) {
				int uu = j+z;
				while (uu > c) uu -= c;
				hh += (char)('0'+s[i][uu]);
			}
		}
		if (q.count(hh)) return;
	}
	/*for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			cout << s[i][j] << " ";
		}
		cout << "\n";
	}
	cout << "\n";*/
	//cout << hh << "\n";
	q.insert(hh);
	cc++;
}

void haku(int y, int x) {
	if (y == r+1) {
		valmis();
		return;
	}
	if (x == c+1) {
		if (!alku(y)) return;
		haku(y+1,1);
		return;
	}
	for (int i = 1; i <= 4; i++) {
		s[y][x] = i;
		haku(y,x+1);
	}
}

void solve(int x) {
	cin >> r >> c;
	cc = 0;
	q.clear();
	haku(1,1);
	cout << "Case #" << x << ": " << cc << "\n";
}

int main() {
	cin >> t;
	for (int i = 1; i <= t; i++) solve(i);
}
