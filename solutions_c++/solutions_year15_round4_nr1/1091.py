#define _USE_MATH_DEFINES
#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <cfloat>
#include <climits>
#include <cstring>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <time.h>
#include <vector>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> i_i;
typedef pair<ll, int> ll_i;
typedef pair<double, int> d_i;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> d_d;
struct edge { int u, v; ll w; };

ll MOD = 1000000007;
ll _MOD = 1000000009;
double EPS = 1e-10;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

bool f(int R, int C, vector<string>& a, int x, int y, int k) {
	for (int _x = x + dx[k], _y = y + dy[k]; _x >= 0 && _x < C && _y >= 0 && _y < R; _x += dx[k], _y += dy[k])
		if (a[_y][_x] != '.')
			return true;
	return false;
}

int main() {
	map<char, int> m;
	m['<'] = 0;
	m['^'] = 1;
	m['>'] = 2;
	m['v'] = 3;
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int R, C; cin >> R >> C;
		vector<string> a(R);
		for (int y = 0; y < R; y++)
			cin >> a[y];
		int cnt = 0;
		bool pos = true;
		for (int y = 0; y < R; y++)
			for (int x = 0; x < C; x++) {
				char c = a[y][x];
				if (c == '.' || f(R, C, a, x, y, m[c])) continue;
				cnt++;
				bool ok = false;
				for (int k = 0; k < 4; k++)
					if (f(R, C, a, x, y, k))
						ok = true;
				if (!ok) pos = false;
			}
			if (pos) printf("Case #%d: %d\n", t, cnt);
			else printf("Case #%d: IMPOSSIBLE\n", t);
	}
}