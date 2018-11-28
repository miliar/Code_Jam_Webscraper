#include <bits/stdc++.h>
using namespace std;
#define oo (1<<30)
#define sz(v) (int)v.size()

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "rt", stdin);
	freopen("test.out", "wt", stdout);

#endif

	int T = 1;
	cin>>T;
	for (int U = 1; U <= T; U++) {
		double time = 0;
		double z = 2;
		double c, f, x;
		cin >> c >> f >> x;

		double mn = 999999999999;

		while (true) {
			if (mn < time)
				break;
			mn = min(mn, (x / z) + time);
			time += (c / z);
			z += f;

		}
		printf("Case #%d: ", U);
		cout << setprecision(7) << fixed << mn << endl;
	}
	return 0;
}
;
