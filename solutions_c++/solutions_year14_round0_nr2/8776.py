#include <bits/stdc++.h>
using namespace std;


int main() {
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	cout << fixed << setprecision(15);
	for (int i = 0; i < T; ++i) {

		long double C, F, X, rate = 2.0, t = 0.0;
		cin >> C >> F >> X;

		while(true) {
			long double t1 = X / rate;
			long double t2 = C / rate + X / (F + rate);
			if (t1 < t2) {
				t += t1;
				break;
			}
			t += C / rate;
			rate += F;
		}

		cout << "Case #" << i + 1 << ": ";

		cout << t;

		cout << "\n";
	}
	return 0;
}
