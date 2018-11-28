#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <list>
#include <iomanip>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <ctime>

#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)
#define sz(a) int(a.size())

using namespace std;

typedef long long li;
typedef long double ld;

typedef pair<int,int> pt;
#define ft first
#define sc second

const int N = 200;
char f[N][N];

string dirs = "<>^v";
int n, m;
int dx[4] = {0, 0, -1, + 1};
int dy[4] = {-1, + 1, 0, 0};


bool read() {
	if (!(cin >> n >> m))
		return false;
	forn(i, n)
		cin >> f[i];
	return true;
}

bool move_while(int i, int j, int d) {
	while (true) {
		int ni = i + dx[d];
		int nj = j + dy[d];

		if (ni < 0 || ni >= n || nj < 0 || nj >= m)
			return false;

		if (f[ni][nj] != '.')
			return true;

		i = ni, j = nj;
	}

	
}

void solve() {
	int res = 0;
	bool bad = false;
	forn(i, n) {
		forn(j, m) {
			if (f[i][j] == '.') continue;

			int d = dirs.find(f[i][j]);
			bool good = false;

			if (!move_while(i, j, d)) {
				forn(d, 4) {
					if (move_while(i, j, d))
						good = true;
				}

				if (good)
					res++;
				else
					bad = true;
			}
		}
	}

	if (bad)
		puts("IMPOSSIBLE");
	else
		printf("%d\n", res);
}

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T = 0;
	cin >> T;

	forn(t, T) {
		assert(read());
		cout << "Case #" << t + 1 << ": ";
		solve();
	}
	
	return 0;
}
