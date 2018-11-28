#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;
#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) a; i < (int) b; ++i)
#define pb push_back
#define ld long double
const int MAXN = 200000;

vector <int> v[2];//, ans[3];

int ans[MAXN];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tk;
	cin >> tk;

	forn(q, tk) {
		ld c, f, x;
		cin >> c >> f >> x;
		ld ans = MAXN;
		ld pr = 2, dt = 0;

		forn(i, MAXN) {
			ld t = dt + x / pr;
			ans = min(ans, t);

			dt += c / pr;
			pr += f;
		}

		printf("Case #%d: %Lf\n", q + 1, ans);
	}

	return 0;
}
