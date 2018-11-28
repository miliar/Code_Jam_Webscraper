#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;
typedef vector<int> vi_;
typedef long long ll_;
ll_ n, y, z;
vi_ v;

void solve() {
	int eat_rate = 0;
	for (int i = 1; i < n; ++i) {
		eat_rate = max(eat_rate, v[i - 1] - v[i]);
	}
	y = 0; z = 0;
	for (int i = 1; i < n; ++i) {
		int d = v[i - 1] - v[i];
		y += (d > 0 ? d : 0);
		z += min(eat_rate, v[i - 1]);
	}
}

int main() {
	freopen("a.in", "r", stdin);
	int t; cin >> t;
	for (int tloop = 0; tloop < t; ++tloop) {
		cin >> n;
		v = vi_(n);
		for (int nloop = 0; nloop < n; ++nloop) cin >> v[nloop];
		solve();
		cout << "Case #" << tloop + 1 << ": " << y << " " << z << endl;
	}
}