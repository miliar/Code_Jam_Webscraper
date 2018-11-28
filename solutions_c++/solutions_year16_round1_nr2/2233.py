#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

const int N = 100;
#define MP make_pair
#define lli long long int

int a[N][N];
int ri[N], ci[N];
int mr = 0;
int mi = 0;
int n;
bool found = false;
vector<vector<int> > v;

void clearFound() {
	mr = mi = 0;
	found = false;
}

void clear() {
	memset(ri, -1, N*sizeof(int));
	memset(ci, -1, N*sizeof(int));	
	clearFound();
}

vector<int> answer;

bool canSetRow(int pos, int i) {
	for (int j = 0; j < pos; ++j) {
		if (a[pos][j] > 0 && a[pos][j] != v[i][j]) {
			return false;
		}
	}
	return true;
}

bool canSetCol(int pos, int i) {
	for (int j = 0; j < pos; ++j) {
		if (a[j][pos] > 0 && a[j][pos] != v[i][j]) {
			return false;
		}
	}
	return true;
}

void setRow(int pos, int i) {
	for (int j = 0; j < n; ++j) a[pos][j] = v[i][j];
	ri[i] = pos;
}

void setCol(int pos, int i) {
	for (int j = 0; j < n; ++j) a[j][pos] = v[i][j];
	ci[i] = pos;
}

bool solve(int pos) {
	if (pos == n) {
		answer.resize(n);
		for (int i = 0; i < n; ++i) answer[i] = (mr ? a[mi][i] : a[i][mi]);
		return true;
	}
	int mv = 3030303;
	for (int i = 0; i < v.size(); ++i) {
		if (ri[i] == -1 && ci[i] == -1) mv = min(mv, v[i][pos]);
	}
	vector<int> mins;
	for (int i = 0; i < v.size(); ++i) {
		if (ri[i] == -1 && ci[i] == -1 && v[i][pos] == mv) mins.push_back(i);
	}
	if (mins.size() > 2) return false;
	if (mins.size() == 1) {
		if (found) return false;

		if (canSetRow(pos, mins[0])) {
			setRow(pos, mins[0]);
			mr = 0; mi = pos; found = 1;
			for (int i = pos + 1; i < n; ++i) a[i][pos] = 0;
			if (solve(pos + 1)) return true;
		}

		if (canSetCol(pos, mins[0])) {
			setCol(pos, mins[0]);
			mr = 1; mi = pos; found = 1;
			for (int i = pos+1; i < n; ++i) a[pos][i] = 0;
			if (solve(pos + 1)) return true;
		}
		clearFound();
		ri[mins[0]] = ci[mins[0]] = -1;

		return false;
	}
	bool fr = canSetRow(pos, mins[0]), fc = canSetCol(pos, mins[0]);
	bool sr = canSetRow(pos, mins[1]), sc = canSetCol(pos, mins[1]);
	if (fr && sc) {
		setRow(pos, mins[0]); setCol(pos, mins[1]);
		if (solve(pos + 1)) return true;
	}
	if (sr && fc) {
		setRow(pos, mins[1]); setCol(pos, mins[0]);
		if (solve(pos + 1)) return true;
	}
	ri[mins[1]] = ci[mins[1]] = ri[mins[0]] = ci[mins[0]] = -1;

	return false;
}

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";

		cin >> n;
		v.clear();
		v.resize(2 * n - 1, vector<int>(n, 0));

		clear();
		for (int i = 0; i < 2 * n -1; ++i) {
			for (int j = 0; j < n; ++j) cin >> v[i][j];
		}
		sort(v.begin(), v.end());
		solve(0);
		for (int i = 0; i < n; ++i) cout << answer[i] << ' ';
		
		cout << endl;
	}
}