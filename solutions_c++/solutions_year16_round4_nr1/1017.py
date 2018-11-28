#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORVEC(it,v) for (auto it=(v).begin(); it != (v).end(); ++it)
#define NUL(arr) memset(arr, 0, sizeof(arr));
#define SORT(x) sort((x).begin(), (x).end());

// 0 = rock, 1 = paper, 2 = scissors
// 0 => 02; R => RS;
// 1 => 10; P => PR;
// 2 => 12; S => PS;

struct cnt {
	int r, p, s; string q;
	cnt(){};
	cnt(int a, int b, int c, string d):r(a),p(b),s(c),q(d){};
};

cnt x[14][3];

int wy[3] = { 0, 0, 1 };
int wz[3] = { 2, 1, 2 };

void precalc()
{
	x[0][0] = cnt(1, 0, 1, "RS");
	x[0][1] = cnt(1, 1, 0, "PR");
	x[0][2] = cnt(0, 1, 1, "PS");
	for (int r=1; r<14; ++r) {
		for (int w=0; w<3; ++w) {
			int y = wy[w];
			int z = wz[w];
			string a = x[r-1][y].q + x[r-1][z].q;
			string b = x[r-1][z].q + x[r-1][y].q;
			if (b < a) swap(a, b);
			x[r][w] = cnt(
				x[r-1][y].r + x[r-1][z].r,
				x[r-1][y].p + x[r-1][z].p,
				x[r-1][y].s + x[r-1][z].s,
				a
			);
		}
	}
}

void solve()
{
	int n, r, p, s;
	cin >> n >> r >> p >> s;
	for (int w=0; w<3; ++w) {
		if (x[n-1][w].r == r && x[n-1][w].p == p && x[n-1][w].s == s) {
			cout << x[n-1][w].q;
			return;
		}
	}
	cout << "IMPOSSIBLE";
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	precalc();
	int t;
	cin >> t;
	for (int i=1; i<=t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}
