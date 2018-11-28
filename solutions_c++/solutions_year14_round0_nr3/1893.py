#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
using namespace std;

int R, C, M;
bool FOUND;
string ANS;
set<string> S;

void mark_edge(string &s, int y, int x)
{
	for (int i = y - 1; i <= y + 1; ++i) {
		if (i < 0 || i >= R) continue;
		for (int j = x - 1; j <= x + 1; ++j) {
			if (j < 0 || j >= C) continue;
			if (s[i * C + j] == '*') s[i * C + j] = '|';
		}
	}
	
	return;
}

int count_mine(string &x) {
	int ret = 0;
	for (int i = 0; i < x.size(); ++i) {
		if (x[i] == '*') ++ret;
	}
	
	return ret;
}

void solve(string x)
{
	if (FOUND) return;
	if (S.find(x) != S.end() ) return;
	S.insert(x);
	
	int cm = count_mine(x);
	if (cm == M) {
		FOUND = true;
		ANS = x;
		return;
	} else if (cm < M) {
		return;
	}
	
	//cout << "solve() - " << x << endl;
	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < C; ++j) {
			if (x[i * C + j] == '|') {
				string y = x;
				y[i * C + j] = '.';
				mark_edge(y, i, j);
				solve(y);
			}
		}
	}
	
	return;
}

int main()
{
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; ++t) {
		cin >> R >> C >> M;
		FOUND = false;
		S.clear();
		
		if (R * C - M == 0) {
			FOUND = false;
		} else if (R * C - M == 1) {
			FOUND = true;
			ANS = string(R * C, '*');
			ANS[0] = 'c';
		} else {
			for (int i = 0; i < R && !FOUND; ++i) {
				for (int j = 0; j < C && !FOUND; ++j) {
					string x(R * C, '*');
					x[i * C + j] = 'c';
					mark_edge(x, i, j);
					solve(x);
				}
			}
		}
		
		cout << "Case #" << t << ":" << endl;
		if (!FOUND) cout << "Impossible" << endl;
		else {
			for (int i = 0; i < R; ++i) {
				string x(C, '*');
				for (int j = 0; j < C; ++j) {
					x[j] = ANS[i * C + j];
					if (x[j] == '|') x[j] = '.';
				}
				cout << x << endl;
			}
		}
	}
	
	return 0;
}
