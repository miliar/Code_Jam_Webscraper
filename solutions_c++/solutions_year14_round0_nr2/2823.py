#include<bits/stdc++.h>
using namespace std;

#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))

const int OO = (int) 2e9;
const double EPS = 1e-9;

int dcmp(long double a, long double b) {
	return fabs(a - b) <= EPS ? 0 : a > b ? 1 : -1;
}

int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	double C, F, X;
	int t;

	cin >> t;

	for (int tt = 1; tt <= t; tt++) {

		cin >> C >> F >> X;

		double ans = X / 2.0;

		double add = 2;

		double sec = C / add;

		for (int f = 1;; f++) {

			add += F;

			double en = (X / add);

			if (dcmp(en + sec, ans) <= 0)
			ans = en + sec;
			else
			break;

			sec += (C / add);

			//	cout << sec << endl;

		}

		printf("Case #%d: ", tt);
		printf("%.7lf\n", ans);

	}

	return 0;
}
