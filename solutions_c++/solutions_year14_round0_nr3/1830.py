#include <iostream>
#include <limits>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <vector>
using namespace std;

int r, c, tot;
char f[10][10];
int o[100][100];
bool v[10][10];

void print(int mx, int my) {
	f[mx][my] = 'c';
	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++)
			cout << f[i][j];
		cout << endl;
	}
}

void dfs2(int x, int y) {
	if (f[x][y] == '*' || v[x][y])
		return;
	v[x][y] = true;
	if (o[x][y] == 0) {
		for (int dx = -1; dx <= 1; dx++)
			for (int dy = -1; dy <= 1; dy++)
				dfs2(x + dx, y + dy);
	} else
		o[x][y] = 0;
}

bool check() {
	for (int i = 1; i <= r; i++)
		for (int j = 1; j <= c; j++)
			o[i][j] = 0;
	for (int i = 1; i <= r; i++)
		for (int j = 1; j <= c; j++)
			if (f[i][j] == '*')
				for (int di = -1; di <= 1; di++)
					for (int dj = -1; dj <= 1; dj++)
						o[i + di][j + dj]++;
	int mx = 1;
	int my = 1;
	int mo = 10;
	for (int i = 1; i <= r; i++)
		for (int j = 1; j <= c; j++)
			if (f[i][j] == '.' && mo > o[i][j]) {
				mo = o[i][j];
				mx = i;
				my = j;
			}

	if (mo > 0) {
		if (tot == r * c - 1) {
			print(mx, my);
			return true;
		} else
			return false;
	}

	for (int i = 1; i <= r; i++)
		for (int j = 1; j <= c; j++)
			v[i][j] = false;
	dfs2(mx, my);
	for (int i = 1; i <= r; i++)
		for (int j = 1; j <= c; j++)
			if (f[i][j] == '.' && o[i][j] > 0)
				return false;

	print(mx, my);
	return true;
}

bool dfs(int x, int y, int k) {
	if (x == r + 1) {
		if (k == tot) {
			return check();
		} else {
			return false;
		}
	}

	int nx = x;
	int ny = y + 1;
	if (ny > c) {
		nx++;
		ny = 1;
	}
	
	if (c * (r - x) + c - y >= tot - k) {
		f[x][y] = '.';
		if (dfs(nx, ny, k))
			return true;
	}

	if (k + 1 <= tot) {
		f[x][y] = '*';
		if (dfs(nx, ny, k + 1))
			return true;
	}

	return false;
}

void work() {
	cin >> r >> c >> tot;
	if (!dfs(1, 1, 0))
		cout << "Impossible" << endl;
}

int main() {
	
	//freopen("G:/1.in", "r", stdin);
	//freopen("G:/1.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": " << endl;
		memset(f, '*', sizeof(f));
		work();
	}
	return 0;
}