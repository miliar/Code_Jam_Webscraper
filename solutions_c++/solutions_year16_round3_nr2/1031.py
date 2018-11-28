#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)n; i++)
#define vec vector
#define ll long long

void pr(vec<vec<int>> l)
{
	rep(i, l.size()) {
		rep(j, l[i].size()) cout << l[i][j];
		cout << endl;
	}
}

int main(void)
{
	int t;
	cin >> t;
	rep(f, t) {
		int b;
		cin >> b;
		ll m;
		cin >> m;

		if (pow(2, b - 2) < m) {
			cout << "Case #" << f + 1 << ": IMPOSSIBLE" << endl;
			continue;
		}
		cout << "Case #" << f + 1 << ": POSSIBLE" << endl;

		vec<vec<int>> l(b, vec<int>(b, 0));
		rep(i, b - 1) rep(j, b - i - 1) l[i][i + j + 1] = 1;
		if (m == pow(2, b - 2)) {
			pr(l);
			continue;
		}

		ll k = (ll)pow(2, b - 3);
		
		rep(i, b - 1) {
			if (m == 0) l[0][i + 1] = 0;
			if (m >= k) m -= k;
			else l[0][i + 1] = 0;
			k /= 2;
		}

		pr(l);
	}
	return 0;

}
