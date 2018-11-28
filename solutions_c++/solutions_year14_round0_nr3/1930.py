#include <iostream>
#include <cstdio>
#include <fstream>

#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <string>
#include <cstring>

#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cassert>
#include <memory.h>
using namespace std;

#define fr(i, n) for (int i = 0; i < (int)(n); i++)
#define fb(i, n) for (int i = n - 1; i >= 0; i--)
#define all(a) (a).begin(), (a).end()
#define _(a, b) memset(a, b, sizeof(a))
#define mp make_pair
#define pb push_back
#define sz(v) ((int)(v).size())

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

inline int ni() { int a; scanf("%d", &a); return a; }
inline double nf() { double a; scanf("%lf", &a); return a; }
template <class T> void out(T a, T b) { bool first = true; for (T i = a; i != b; i++) { if (!first) printf(" "); first = false; cout << *i; } puts(""); }
template <class T> void outl(T a, T b) { for (T i = a; i != b; i++) cout << *i << "\n"; } 

const int MAXN = 7;

int T;
int R, C, M;

char d[MAXN][MAXN];
bool u[MAXN][MAXN];

bool z(int x, int y) {
	return d[x][y] != '*';
}

bool zz(int x, int y) {
	return !u[x][y] && (1 <= x && x <= R) && (1 <= y && y <= C);
}

bool start(int x, int y) {
	fr(i, R)
		fr(j, C)
			u[i + 1][j + 1] = false;
	queue<pii> q;
	q.push(mp(x, y));
	u[x][y] = true;
	int val = 1;
	while (!q.empty()) {
		pii cur = q.front();
		q.pop();
		x = cur.first, y = cur.second;
		int c = z(x - 1, y - 1) + z(x - 1, y) + z(x - 1, y + 1) + z(x, y - 1) + z(x, y + 1) + z(x + 1, y - 1) + z(x + 1, y) + z(x + 1, y + 1);
		if (c == 8) {
			if (zz(x - 1, y - 1)) {
				u[x - 1][y - 1] = true;
				val++;
				q.push(mp(x - 1, y - 1));
			}
			if (zz(x - 1, y)) {
				u[x - 1][y] = true;
				val++;
				q.push(mp(x - 1, y));
			}
			if (zz(x - 1, y + 1)) {
				u[x - 1][y + 1] = true;
				val++;
				q.push(mp(x - 1, y + 1));
			}
			if (zz(x, y - 1)) {
				u[x][y - 1] = true;
				val++;
				q.push(mp(x, y - 1));
			}
			if (zz(x, y + 1)) {
				u[x][y + 1] = true;
				val++;
				q.push(mp(x, y + 1));
			}
			if (zz(x + 1, y - 1)) {
				u[x + 1][y - 1] = true;
				val++;
				q.push(mp(x + 1, y - 1));
			}
			if (zz(x + 1, y)) {
				u[x + 1][y] = true;
				val++;
				q.push(mp(x + 1, y));
			}
			if (zz(x + 1, y + 1)) {
				u[x + 1][y + 1] = true;
				val++;
				q.push(mp(x + 1, y + 1));
			}
		}
	}
	return val == R * C - M;
}

bool find() {
	fr(i, R)
		fr(j, C)
			if (d[i + 1][j + 1] == '.') {
				fr(k, MAXN)
					fr(l, MAXN)
						u[k][l] = false;
				d[i + 1][j + 1] = 'c';
				if (start(i + 1, j + 1))
					return true;
				d[i + 1][j + 1] = '.';
			}
	return false;
}

bool check(int x, int y, int all) {
	if (all + (R - x) * C + (C - y + 1) < M)
		return false;
	if (x == R && y == C) {
		if (all < M) {
			d[x][y] = '*';
			if (find())
				return true;
			d[x][y] = '.';
		} else if (find())
			return true;
	} else {
		if (y == C) {
			if (check(x + 1, 1, all))
				return true;
			d[x][y] = '*';
			if (all < M && check(x + 1, 1, all + 1))
				return true;
			d[x][y] = '.';
		} else {
			if (check(x, y + 1, all))
				return true;
			d[x][y] = '*';
			if (all < M && check(x, y + 1, all + 1))
				return true;
			d[x][y] = '.';								
		}
	}
	return false;
}

int main() {	
	freopen("minesweeper.in", "r", stdin);
	freopen("minesweeper.out", "w", stdout);
	T = ni();
	fr(test, T) {
		R = ni();
		C = ni();
		M = ni();
		fr(i, MAXN)
			fr(j, MAXN)
				d[i][j] = '.';
		if (check(1, 1, 0)) {
			printf("Case #%d:\n", test + 1);
			fr(i, R) {
				fr(j, C) {
					cout << d[i + 1][j + 1];
				}
				cout << endl;
			}
		} else {
			printf("Case #%d:\nImpossible\n", test + 1);
		}
	}  
}
        