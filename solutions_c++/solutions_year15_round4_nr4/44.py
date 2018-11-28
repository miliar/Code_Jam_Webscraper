#include <iostream>
#include <set>
#include <complex>
#include <cassert>
#include <vector>
#include <iomanip>
#include <sstream>
#include <map>

using namespace std;

int R, C;
typedef array<array<int, 6>, 6> SD;
SD V;

set<SD> xd;

bool ok() {
	vector<int> vals;
	for(int i = 0; i < R; ++i) {
	for(int j = 0; j < C; ++j) {
		int val = V[i][j];
		if(val == 0) continue;
		vals.clear();
		if(i != 0) vals.push_back(V[i-1][j]);
		if(i != R - 1) vals.push_back(V[i+1][j]);
		vals.push_back(V[i][(j + C - 1) % C]);
		vals.push_back(V[i][(j + 1) % C]);
		
		int mincount = 0;
		int maxcount = 0;
		for(int x : vals) {
			if(x == val) {
				++mincount;
				++maxcount;
			} else if(x == 0) {
				++maxcount;
			}
		}
		if(val < mincount || val > maxcount) return false;
	}
	}
	return true;
}

void rotate() {
	SD X = V;
	for(int i = 0; i < R; ++i) {
	for(int j = 0; j < C; ++j) {
		V[i][j] = X[i][(j + 1) % C];
	}
	}
}

void lol(int i, int j) {
	if(j == C) {
		lol(i + 1, 0);
		return;
	}
	if(i == R) {
		if(!ok()) return;
		SD best = V;
		for(int a = 0; a < C; ++a) {
			rotate();
			best = min(best, V);
		}
		xd.insert(best);
		return;
	}
	
	if(!ok()) return;
	for(int x = 1; x <= 4; ++x) {
		V[i][j] = x;
		lol(i, j + 1);
	}
	V[i][j] = 0;
}

int main() {
	cin.sync_with_stdio(false);
	
	int Te;
	cin >> Te;
	for(int T = 0; T < Te; ++T) {
		xd.clear();
		cin >> R >> C;
		
		for(int i = 0; i < R; ++i) {
		for(int j = 0; j < C; ++j) {
			V[i][j] = 0;
		}
		}
		
		lol(0, 0);
		cout << "Case #" << T + 1 << ": " << xd.size() << '\n';
	}
	
	return 0;
}
