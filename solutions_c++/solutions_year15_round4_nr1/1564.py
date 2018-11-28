#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>
#include <vector>
#include <fstream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <unordered_set>
#include <unordered_map>
using namespace std;
#define LL long long
#define file freopen("input.txt" ,"r", stdin); freopen("output.txt", "w", stdout);
#define faster ios::sync_with_stdio(0);

char a[101][101];

int used[101][101];
bool pos = true;
int n, m;
int ans = 0;

void rec(int x, int y) {

	used[x][y] = 1;
	int l = -1, r = -1, u = -1, d = -1;
	for (int i = x - 1; i >= 0; i--) {
		if (a[i][y] != '.') {
			u = i;
			break;
		}
	}
	for (int i = x + 1; i < n; i++) {
		if (a[i][y] != '.') {
			d = i;
			break;
		}
	}
	for (int j = y - 1; j >= 0; j--) {
		if (a[x][j] != '.') {
			l = j;
			break;
		}
	}
	for (int j = y + 1; j < m; j++) {
		if (a[x][j] != '.') {
			r = j;
			break;
		}
	}

	if (u == -1 && d==-1 && l==-1 && r==-1) {
		pos = false;
		return;
	}


	if (a[x][y] == '^' && u != -1) {
		if (used[u][y]) return;
		rec(u, y);
		return;
	}
	if (a[x][y] == 'v' && d != -1) {
		if (used[d][y]) return;
		rec(d, y);
		return;
	}
	if (a[x][y] == '<' && l != -1) {
		if (used[x][l]) return ;
		rec(x, l);
		return;
	}
	if (a[x][y] == '>' && r != -1) {
		if (used[x][r]) return ;
		rec(x, r);
		return;
	}

	if (l != -1) {
		ans++;
		a[x][y] = '<';
		if (used[x][l]) return;
		rec(x, l);
		return;
	}
	if (r != -1) {
		ans++;
		a[x][y] = '>';
		if (used[x][r]) return;
		rec(x, r);
		return;
	}

	if (u != -1) {
		ans++;
		a[x][y] = '^';
		if (used[u][y]) return;
		rec(u, y);
		return;
	}
	if (d != -1) {
		ans++;
		a[x][y] = 'v';
		if (used[d][y]) return;
		rec(d, y);
		return;
	}

	 
}
int main() {
	file;
	faster;

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				char x;
				cin >> x;
				a[i][j] = x;
			}
		}

		for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			used[i][j] = 0;
		}}
		ans = 0;
		pos = 1;

		for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (a[i][j] != '.' && used[i][j] == 0) {
				rec(i, j);
			}
		}}

		if (pos == false) {
			cout << "Case #" << t << ": IMPOSSIBLE\n";
		} else {
			cout << "Case #" << t << ": " << ans << '\n';
		}
	}
}


