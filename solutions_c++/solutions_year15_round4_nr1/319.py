#include "bits/stdc++.h"
 
using namespace std;
 
#define debug(x) cerr << "DEBUG: " << #x << " = " << x << endl
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back
#define PATH "C:\\Users\\ValenKof\\Desktop\\"
 
template<typename T> inline void mn(T& x, const T& y) { if (y < x) x = y; }
template<typename T> inline void mx(T& x, const T& y) { if (x < y) x = y; }
template<typename T> inline int sz(const T& x) { return x.size(); }
 
typedef unsigned char uchar;
 
// SOLUTIONS BEGINS HERE

int n, m;

bool inside(int i, int j)
{ return 0 <= i && i < n && 0 <= j && j < m; }

pair<int, int> dir(char c)
{
	switch (c) {
		case '>': return {0, +1};
		case '<': return {0, -1};
		case '^': return {-1, 0};
		case 'v': return {+1, 0};
	}
	return {0, 0};
}

bool dead(int i, int j, const vector<string>& g, pair<int, int> d) {
	i += d.first;
	j += d.second;
	while (inside(i, j) && g[i][j] == '.') {
		i += d.first;
		j += d.second;
		// debug(i);
	}
	if (!inside(i, j)) {
		return true;
	}
	return false;
}

int solve() {
	cin >> n >> m;
	vector<string> g(n);
	forn (i, n) {
		cin >> g[i];
	}
	
	forn (i, n) {
		forn (j, m) {
			if (g[i][j] != '.') {
				bool full = dead(i, j, g, {0, +1}) &&
					dead(i, j, g, {0, -1}) &&
					dead(i, j, g, {-1, 0}) &&
					dead(i, j, g, {+1, 0});
				if (full) {
					return -1;
				}
			}
		}
	}
	
	
	int ans = 0;
	while (true) {
		bool changed = false;
		forn (i, n) {
			forn (j, m) {
				if (g[i][j] != '.' && g[i][j] != '*') {
					if (dead(i, j, g, dir(g[i][j]))) {
						g[i][j] = '*';
						changed = true;
						ans++;
					}	
				}
			}
		}
		if (!changed) {
			break;
		}
	}
	
	return ans;
	
	
}
 
int main() {
	freopen(PATH"A-large.in", "r", stdin);
	freopen(PATH"out.txt", "w", stdout);
	int nTests;
	cin >> nTests;
	forn (i, nTests) {
		cout << "Case #" << (i + 1) << ": ";
		int ans = solve();
		if (ans == -1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << ans;
		}
		cout << endl;
	}	
	return 0;
}