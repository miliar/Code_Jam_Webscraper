#define _USE_MATH_DEFINES
#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <cfloat>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <queue>
#include <random>
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

int INF = INT_MAX / 2;
ll MOD = 1000000007;
ll _MOD = 1000000009;
double EPS = 1e-10;

int dy[4] = {0, -1, 0, 1};
int dx[4] = {-1, 0, 1, 0};

struct unko { int y, x, k; };

unko f(int H, int W, int i) {
	if (i < W) return unko{0, i, 3};
	i -= W;
	if (i < H) return unko{i, W - 1, 0};
	i -= H;
	if (i < W) return unko{H - 1, W - 1 - i, 1};
	i -= W;
	if (i < H) return unko{H - 1 - i, 0, 2};
}

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		printf("Case #%d:\n", t);
		int H, W; cin >> H >> W;
		int N = (H + W) * 2;
		vector<int> p(N);
		for (int t = 0; t < N / 2; t++) {
			int i, j; cin >> i >> j;
			i--; j--;
			p[i] = j;
			p[j] = i;
		}
		for (int S = 0; S < 1<<(H * W); S++) {
			vector<vector<int> > a(H, vector<int>(W));
			for (int i = 0; i < H * W; i++)
				a[i / W][i % W] = 1 + (S>>i & 1);
			bool wei = true;
			for (int i = 0; i < N; i++) {
				int j = p[i];
				unko s = f(H, W, i), t = f(H, W, j);
				t.k = (t.k + 2) % 4;
				vector<vector<vector<int> > > d(H, vector<vector<int> >(W, vector<int>(4, INF)));
				queue<unko> q;
				d[s.y][s.x][s.k] = 0;
				q.push(s);
				bool ok = false;
				while (!q.empty()) {
					unko z = q.front(); q.pop();
					int y = z.y, x = z.x, k = z.k;
					vector<int> ks;
					int w = a[y][x];
					if (k == 0) {
						if (w != 1) ks.push_back(1);
						if (w != 2) ks.push_back(3);
					}
					if (k == 1) {
						if (w != 1) ks.push_back(0);
						if (w != 2) ks.push_back(2);
					}
					if (k == 2) {
						if (w != 1) ks.push_back(3);
						if (w != 2) ks.push_back(1);
					}
					if (k == 3) {
						if (w != 1) ks.push_back(2);
						if (w != 2) ks.push_back(0);
					}
					for (int _k: ks) {
						if (y == t.y && x == t.x && _k == t.k) {
							ok = true;
							goto UNCHI;
						}
						int _y = y + dy[_k], _x = x + dx[_k];
						if (_y >= 0 && _y < H && _x >= 0 && _x < W && d[_y][_x][_k] > d[y][x][k] + 1) {
							unko _z{_y, _x, _k};
							d[_y][_x][_k] = d[y][x][k] + 1;
							q.push(_z);
						}
					}
				}
				UNCHI:;
				if (!ok) {
					wei = false;
					break;
				}
			}
			if (wei) {
				for (int y = 0; y < H; y++) {
					for (int x = 0; x < W; x++)
						cout << "//\\"[a[y][x]];
					cout << endl;
				}
				goto UNKO;
			}
		}
		cout << "IMPOSSIBLE" << endl;
		UNKO:;
		/*
		vector<bool> used(N);
		vector<vector<int> > a(H, vector<int>(W));
		for (int t = 0; t < N / 2; t++) {
			int i, j;
			for (i = 0; i < N; i++) {
				for (j = (i + 1) % N; used[j]; j = (j + 1) % N);
				if (j == p[i]) break;
			}
			if (i == N) {
				cout << "IMPOSSIBLE" << endl;
				goto UNKO;
			}
			used[i] = used[j] = true;
			unko s = f(H, W, i), t = f(H, W, j);
			t.k = (t.k + 2) % 4;
			vector<vector<vector<int> > > d(H, vector<vector<int> >(W, vector<int>(4, INF)));
			vector<vector<vector<unko> > > prev(H, vector<vector<unko> >(W, vector<unko>(4)));
			queue<unko> q;
			d[s.y][s.x][s.k] = 0;
			prev[s.y][s.x][s.k] = unko{-1, -1, -1};
			q.push(s);
			while (!q.empty()) {
				unko z = q.front(); q.pop();
				int y = z.y, x = z.x, k = z.k;
				vector<int> ks;
				int w = a[y][x];
				if (k == 0) {
					if (w != 1) ks.push_back(1);
					if (w != 2) ks.push_back(3);
				}
				if (k == 1) {
					if (w != 1) ks.push_back(0);
					if (w != 2) ks.push_back(2);
				}
				if (k == 2) {
					if (w != 1) ks.push_back(3);
					if (w != 2) ks.push_back(1);
				}
				if (k == 3) {
					if (w != 1) ks.push_back(2);
					if (w != 2) ks.push_back(0);
				}
				for (int _k: ks) {
					if (y == t.y && x == t.x && _k == t.k) {
						prev[y][x][_k] = z;
						goto UNCHI;
					}
					int _y = y + dy[_k], _x = x + dx[_k];
					if (_y >= 0 && _y < H && _x >= 0 && _x < W && d[_y][_x][_k] > d[y][x][k] + 1) {
						unko _z{_y, _x, _k};
						d[_y][_x][_k] = d[y][x][k] + 1;
						prev[_y][_x][_k] = z;
						q.push(_z);
					}
				}
			}
			cout << "IMPOSSIBLE" << endl;
			goto UNKO;
			UNCHI:;
			for (;;) {
				int pk = t.k;
				t = prev[t.y][t.x][t.k];
				if (t.k == -1) break;
				if (t.k == 0 && pk == 3) a[t.y][t.x] = 1;
				if (t.k == 0 && pk == 1) a[t.y][t.x] = 2;
				if (t.k == 1 && pk == 2) a[t.y][t.x] = 1;
				if (t.k == 1 && pk == 0) a[t.y][t.x] = 2;
				if (t.k == 2 && pk == 1) a[t.y][t.x] = 1;
				if (t.k == 2 && pk == 3) a[t.y][t.x] = 2;
				if (t.k == 3 && pk == 0) a[t.y][t.x] = 1;
				if (t.k == 3 && pk == 2) a[t.y][t.x] = 2;
			}
		}
		for (int y = 0; y < H; y++) {
			for (int x = 0; x < W; x++)
				cout << "//\\"[a[y][x]];
			cout << endl;
		}
		UNKO:;
		*/
	}
}
