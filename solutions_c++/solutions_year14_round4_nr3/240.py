#include <iostream>
#include <algorithm>

using namespace std;

int w, h, b;
char r[100][500];

int dx[4] = { 0, -1,  0, 1 };
int dy[4] = { 1,  0, -1, 0 };

void print() {
	cout << endl;
	for (int y=h-1; y>=0; --y) {
		for (int x=0; x<w; x++) {
			cout << r[x][y];
		}
		cout << endl;
	}
	cout << endl;
}

int flow(int x, int y, int d, char c) {
	r[x][y] = c;
	if (y == h-1) return 1;
	for (int z=5; z>=2; z--) {
		int nd = (d + z) % 4;
		int nx = x + dx[nd];
		int ny = y + dy[nd];
		if (nx >= 0 && ny >= 0 && nx < w && ny < h && r[nx][ny] == '.') {
			int f = flow(nx, ny, nd, c);
			if (f == 1) return 1;
		}
	}
	return 0;
}

void solve() {
	cin >> w >> h >> b;
	fill_n(&r[0][0], 100*500, '.');
	for (int i=0; i<b; i++) {
		int x0, y0, x1, y1;
		cin >> x0 >> y0 >> x1 >> y1;
		for (int x=x0; x<=x1; x++) {
			for (int y=y0; y<=y1; y++) {
				r[x][y] = '#';
			}
		}
	}
	int f = 0;
	char cf = 'a';
	for (int s=0; s<w; s++) {
		f += flow(s, 0, 0, cf);
	}
	//print();
	cout << f;
}

int main() {
	int t;
	cin >> t;
	for (int cn=1; cn<=t; cn++) {
		cout << "Case #" << cn << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}