/*
 * c.cpp
 *
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) {}

int r, c, m;
int start;
vector<bool> grid;
vector<int> label;
vector<vector<int> > adj;

bool ispossible() {
	label.assign(r*c, 0);
	forn(u, r*c) {
		if (grid[u]) {
			foreach(it, adj[u]) {
				++label[*it];
			}
		}
	}
	vector<bool> marked(r*c, false);
	stack<int> s;
	forn(u, r*c) {
		if (not grid[u] && label[u] == 0) {
			marked[u] = true;
			s.push(u);
			start = u;
			break;
		}
	}
	// No cell are labeled 0
	if (s.empty()) {
		if (r*c - m >= 2) {
			return false;
		} else {
			forn(u, r*c) {
				if (not grid[u]) {
					start = u;
				}
			}
			return true;
		}
	}
	// Explore adjacent cells
	while (not s.empty()) {
		int u = s.top(); s.pop();
		foreach(it, adj[u]) {
			int v = *it;
			if (not marked[v]) {
				marked[v] = true;
				// Candidate for further exploration?
				if (not grid[v] && label[v] == 0) {
					s.push(v);
				}
			}
		}
	}
	forn(u, r*c) {
		if (not grid[u] && not marked[u])
			return false;
	}
	return true;
}

bool recurse(int i, int k) {
	if (i == r * c) {
		return ((k == m) && ispossible());
	} else {
		if (k < m) {
			grid[i] = true;
			if (recurse(i + 1, k + 1)) {
				return true;
			}
			grid[i] = false;
		}
		if (recurse(i + 1, k)) {
			return true;
		}
		return false;
	}
}

void build() {
	grid.assign(r*c, false);
	adj.assign(r*c, vector<int> ());
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			for (int x = -1; x <= 1; ++x) {
				for (int y = -1; y <= 1; ++y) {
					if (x == 0 && y == 0)
						continue;
					if (i+x >= 0 && i+x < r && j+y >= 0 && j+y < c) {
						adj[i*c+j].push_back((i+x)*c+j+y);
					}
				}
			}
		}
	}
}

int main(void) {
	int t; cin >> t;
	forn(k, t) {
		cin >> r >> c >> m;
		build();
		cout << "Case #" << (k+1) << ": " << endl;
		if (recurse(0, 0)) {
			forn(i, r) {
				forn(j, c) {
					if (start == i*c+j) {
						cout << 'c';
					} else if (grid[i*c+j]) {
						cout << '*';
					} else {
						cout << '.';
					}
				}
				cout << endl;
			}
		} else {
			cout << "Impossible" << endl;
		}
	}
	return 0;
}
