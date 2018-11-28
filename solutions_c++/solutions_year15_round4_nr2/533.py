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

const int N = 1000;
int n;
ld r[N], c[N], v, x;


bool read() {
	if (!(cin >> n))
		return false;

	cin >> v >> x;
	//v *= 10000;
	//x *= 10000;

	forn(i, n) {
		cin >> r[i] >> c[i];
		//r[i] *= 10000;
		//c[i] *= 10000;
	}
	return true;
}

const ld EPS = 0;

void solve() {
	ld res = 1e300;

	forn(i, n)
		if (c[i] == x)
			res = min(res, v / r[i]);

	forn(i, n)
		forn(j, n)
			if (i != j && c[i] == c[j] && c[i] == x)
				res = min(res, v / (r[i] + r[j]));

	forn(i, n) {
		if (c[i] <= x) {
			forn(j, n) {
				if (c[j] >= x && fabsl(c[i] - c[j]) > EPS) {
					ld v1 =   v * (x - c[i]) / (c[j] - c[i]);
					ld v2 = v - v1;
					ld t = max(v1 / r[j], v2 / r[i]);
					
					if (v1 < 0 || v2 < 0)
						continue;
					res = min(res, t);
				}
			}
		}
	}

	if (res < 1e300 / 2)
		cout << fixed << setprecision(8) << res << endl;
	else
		cout << "IMPOSSIBLE\n";
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
