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

int T;
int N, M;
vector<vi> v;
vector<vector<bool> > u;
vi x, y;

const char *solve() {
	cin >> N >> M;
	v.clear(); u.clear();
	v.assign(N, vector<int>(M));
	u.assign(N, vector<bool>(M, false));
	fr(i, N)
		fr(j, M)
			cin >> v[i][j];
	x.assign(N, -1);
	y.assign(M, -1);
	fr(i, N) {
		fr(j, M) {
			int mi = -1, mj = -1, val = 0;
			fr(k, N) {
				fr(l, M) {
					if (!u[k][l] && (mi == -1 || val < v[k][l])) {
						mi = k, mj = l, val = v[k][l];
					}
				}
			}
			u[mi][mj] = true;
			bool flag = false;
			if (x[mi] == -1 || x[mi] == val)
				flag = true, x[mi] = val;
			if (y[mj] == -1 || y[mj] == val)
				flag = true, y[mj] = val;
			if (!flag) {
				return "NO";
			}											
		}
	}				
	return "YES";
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	fr(test, T) {
		printf("Case #%d: %s\n", test + 1, solve());
	}	  
}
        