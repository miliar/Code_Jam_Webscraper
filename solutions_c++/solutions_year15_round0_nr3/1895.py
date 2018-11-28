
//#pragma warning(disable:4996)
#pragma once

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int abs(int n) {
	if (n < 0) return -n;
	return n;
}

int sgn(int n) {
	if (n > 0) return 1;
	if (n < 0) return -1;
	return 0;
}

const int qsize = 5;
vector<int> alp;
int table[5][5];

void init() {
	alp.resize(256, 0);
	alp['i'] = 2;
	alp['j'] = 3;
	alp['k'] = 4;
	for (int i = 1; i <= 4; ++i) {
		table[1][i] = table[i][1] = i;
	}
	table[2][2] = -1; table[2][3] = 4;  table[2][4] = -3;
	table[3][2] = -4; table[3][3] = -1; table[3][4] = 2;
	table[4][2] = 3;  table[4][3] = -2; table[4][4] = -1;
}

const int maxn = 10000;
int flag[3][maxn + 12];

bool solve(const string& s, int n) {
	memset(flag, 0, sizeof(flag));
	if (n < 3) return false;
	int res = 1;
	int a;
	int b;
	for (int i = 0; i < n; ++i) {
		a = abs(res);
		b = alp[s[i]];
		res = sgn(res) * table[a][b];
		if (res == alp['i']) {
			flag[0][i] = 1;
		}
		if (i > 0) {
			flag[0][i] |= flag[0][i-1];
		}
		if (res == alp['k']) {
			flag[1][i] = 1;
		}
	}
	res = 1;
	for (int i = n - 1; i >= 0; --i) {
		a = alp[s[i]];
		b = abs(res);
		res = sgn(res) * table[a][b];
		if (res == alp['k']) {
			flag[2][i] = 1;
		}
	}
	for (int i = 1; i + 1 < n; ++i) {
		if (flag[1][i] && flag[0][i-1] && flag[2][i+1]) {
			return true;
		}
	}
	return false;
}

int main () {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	init();

	int test;
	cin >> test;
	int L, X;
	string s;
	string pat;
	bool ans;
	for (int t = 1; t <= test; ++t) {
		cin >> L >> X;
		cin >> ws >> pat;
		s = pat;
		for (int i = 1; i < X; ++i) {
			s.append(pat);
		}
		ans = solve(s, L * X);
		cout << "Case #" << test << ": ";
		cout << (ans ? ("YES") : ("NO"));
		cout << "\n";
	}

	return 0;
}