#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>

using namespace std;

int n;
int m;

struct line {
	int h[55];
};
bool operator<(const struct line &a, const struct line &b)
{
	for (int i=0; i<n; ++i) {
		if (a.h[i] < b.h[i]) return true;
		if (a.h[i] > b.h[i]) return false;
	}
	return false;
}

line a[55*4];
int map[55][55];

int missing_row = -1;
int missing_col = -1;

bool ok_fill_row(int row, int p)
{
	if (row > n) return false;
	if (row) {
		int r = row-1;
		if (missing_row == r)
			r--;
		if (r >= 0)
			for (int i=0; i<n; ++i)
				if (a[p].h[i] <= map[r][i])
					return false;
	}
	for (int i=0; i<n; ++i) {
		if (map[row][i] && map[row][i] != a[p].h[i])
			return false;
	}
	return true;
}
void fill_row(int row, int p, int *filled)
{
	for (int i=0; i<n; ++i)
		filled[i] = 0;
	for (int i=0; i<n; ++i) {
		if (map[row][i] == 0) {
			filled[i] = 1;
			map[row][i] = a[p].h[i];
		}
	}
}

void unfill_row(int row, int *filled)
{
	for (int i=0; i<n; ++i) {
		if (filled[i]) {
			map[row][i] = 0;
		}
	}
}

bool ok_fill_col(int col, int p)
{
	if (col > n) return false;
	if (col) {
		int c = col - 1;
		if (missing_col == c)
			c--;
		if (c >= 0)
			for (int i=0; i<n; ++i)
				if (a[p].h[i] <= map[i][c])
					return false;
	}
	for (int i=0; i<n; ++i) {
		if (map[i][col] && map[i][col] != a[p].h[i])
			return false;
	}
	return true;
}
void fill_col(int col, int p, int *filled)
{
	for (int i=0; i<n; ++i)
		filled[i] = 0;
	for (int i=0; i<n; ++i) {
		if (map[i][col] == 0) {
			filled[i] = 1;
			map[i][col] = a[p].h[i];
		}
	}
}

void unfill_col(int col, int *filled)
{
	for (int i=0; i<n; ++i) {
		if (filled[i]) {
			map[i][col] = 0;
		}
	}
}

int fill(int row, int col, int i)
{
	int filled[55];
	if (row > n) return 0;
	if (col > n) return 0;
	if (row == n && col == n) {
		if (i != 2*n-1)
			return 0;
		return 1;
	}
	// try fill row
	if (ok_fill_row(row, i)) {
		fill_row(row, i, filled);
		if (fill(row+1, col, i+1))
			return 1;
		unfill_row(row, filled);
	} else if (missing_row == -1 && missing_col == -1) {
		missing_row = row;
		if (fill(row+1, col, i))
			return 1;
		missing_row = -1;
	}
	if (ok_fill_col(col, i)) {
		fill_col(col, i, filled);
		if (fill(row, col+1, i+1))
			return 1;
		unfill_col(col, filled);
	} else if (missing_row == -1 && missing_col == -1) {
		missing_col = col;
		if (fill(row, col+1, i))
			return 1;
		missing_col = -1;
	}
	return 0;
}

void solve(int no)
{
	cin >> n;
	memset(map, 0, sizeof(map));
	memset(a, 0, sizeof(a));
	missing_row = -1;
	missing_col = -1;
	for (int i=0; i<2*n-1; ++i) {
		for (int j=0; j<n; ++j) {
			cin >> a[i].h[j];
		}
	}
	sort(a, a+2*n-1);
	fill(0, 0, 0);
	cout << "Case #" << no << ":";
	if (missing_row != -1) {
		int i = missing_row;
		for (int j=0; j<n; ++j) {
			cout << ' ' << map[i][j];
		}
		cout << endl;
	} else if (missing_col != -1) {
		int j = missing_col;
		for (int i=0; i<n; ++i) {
			cout << ' ' << map[i][j];
		}
		cout << endl;
	}
#if 0
	for (int i=0; i<n; ++i) {
		for (int j=0; j<n; ++j) {
			cout << map[i][j] <<' ' ;
		}
		cout << endl;
	}
#endif
}

int main()
{
	int T;
	cin >> T;
	for (int i=0; i<T; ++i)
		solve(i+1);
	return 0;
}
