/*
 * =====================================================================================
 *
 *       Filename:  B.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/13/2013 02:44:37 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Lei Zhang (antiAgainst), antiagainst@gmail.com
 *   Organization:  University of Waterloo
 *
 * =====================================================================================
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

struct Pos {
	int row, col, value;
	Pos(int a, int b, int c): row(a), col(b), value(c) {}
};

struct Comp {
	bool operator() (const Pos a, const Pos b) {
		return a.value > b.value;
	}
} comp;

bool check(vector<Pos>& loc, int m, int n) {
	int row[m];
	int col[n];
	memset(row, -1, m * sizeof(int));
	memset(col, -1, n * sizeof(int));
	vector<Pos>::iterator it;
	int i, j, val;
	for (it = loc.begin(); it != loc.end(); it++) {
		i = it->row;
		j = it->col;
		val = it->value;
		if (row[i] == -1) row[i] = val;
		if (col[j] == -1) col[j] = val;
		if (row[i] > val && col[j] > val) return false;
	}
	return true;
}

int main() {
	int tc;
	int m, n;
	int data;
	vector<Pos> loc;

	cin >> tc;
	for (int ti = 0; ti < tc; ti++) {
		cin >> m >> n;
		loc.clear();
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++) {
				cin >> data;
				loc.push_back(Pos(i, j, data));
			}
		sort(loc.begin(), loc.end(), comp);
		cout << "Case #" << ti + 1 << ": ";
		if (check(loc, m, n)) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	return 0;
}

