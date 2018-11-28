#include <iostream>
#include <vector>
// #include <algorithm>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int z = 1; z <= t; ++z) {
		int d;
		cin >> d;
		vector<int> m;
		int mx = 0;
		for (int i = 0; i < d; ++i) {
			int p;
			cin >> p;
			m.push_back(p);
			mx = max(mx, p);
		}
		int res = mx;
		for (int nr = 1; nr <= mx; ++nr) {
			int r = nr;
			for (int i = 0; i < d; ++i) {
				if (m[i] > nr) {
					int l = (m[i] + nr - 1) / nr;
					r += l - 1;
				}
			}
			res = min(res, r);
		}
		cout << "Case #" << z << ": " << res << endl;
	}
}