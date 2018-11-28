#include <iostream>
#include <string>
#include <vector>

using namespace std;

int sqr(int x) {return x * x;}

void solve() {
	int n, s;
	cin >> n >> s;
	cerr << n << ' ' << s << endl;
	int x[1000], y[1000], z[1000];
	for (int i = 0; i < n; ++i) {
		cin >> x[i] >> y[i] >> z[i];
		int t; cin >> t >> t >> t;
	}

	double l = 0;
	double r = 2000;

	for (int i = 0; i < 100; ++i) {
		double m = (l + r) / 2;
		vector<int> q;
		vector<int> w(n);
		w[0] = 1;
		q.push_back(0);
		for (int qi = 0; w[1] == 0 && qi < q.size(); ++qi) {
			int c = q[qi];
			for (int j = 0; j < n; ++j) {
				if (w[j] == 0 && sqr(x[c] - x[j]) + sqr(y[c] - y[j]) + sqr(z[c] - z[j]) <= m * m) {
					w[j] = 1;
					q.push_back(j);
				}
			}
		}
		if (w[1]) {
			r = m;
		} else {
			l = m;
		}
	}


	double ans = (l + r) / 2;

	static int test_id;
	cout << fixed;
	cout.precision(10);
	cout << "Case #" << ++test_id << ": " << ans << endl; 
}

int main() {
	int t; cin >> t;
	while (t --> 0)
		solve();
	return 0;
}
