#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int,int> pii;
typedef vector<vector<int> > graph;

const double pi = acos(-1.0);

#define oned(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define twod(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

#define MAXN 105

int TESTS, CASE;

int n, m, a[MAXN][MAXN], b[MAXN][MAXN];

void solve() {
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			b[i][j] = 100;
		}
	}
	
	for(int i = 0; i < n; i++) {
		int mx = 0;
		for(int j = 0; j < m; j++) {
			mx = max(mx, a[i][j]);
		}
		for(int j = 0; j < m; j++) {
			b[i][j] = min(b[i][j], mx);
		}
	}
	
	for(int j = 0; j < m; j++) {
		int mx = 0;
		for(int i = 0; i < n; i++) {
			mx = max(mx, a[i][j]);
		}
		for(int i = 0; i < n; i++) {
			b[i][j] = min(b[i][j], mx);
		}
	}
	
	cout << "Case #" << CASE << ": ";
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			if(a[i][j] != b[i][j]) {
				cout << "NO" << endl;
				return;
			}
		}
	}
	cout << "YES" << endl;
}

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	cin.sync_with_stdio(false);
	cin >> TESTS;
	for(CASE = 1; CASE <= TESTS; CASE++) {
		cin >> n >> m;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				cin >> a[i][j];
			}
		}
		solve();
	}
}
