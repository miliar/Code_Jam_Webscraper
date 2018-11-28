#include <iostream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int n;
vector<int> a[55], b[55];
int sum[55], sum_b[55];

vector<int> solve() {
	int sz = 2 * n - 1; 
	int hi = 1 << sz;
	for (int msk = 1; msk < hi; ++msk) {
		if (__builtin_popcount(msk) != n)
			continue;
		
		memset(sum_b, 0, sizeof(sum_b));
		set<int> fg;
		for (int i = 0; i < sz; ++i) {
			if (msk & (1 << i)) {
				for (int j = 0; j < n; ++j) {
					sum_b[j] += a[i][j];
				}
			} else {
				fg.insert(sum[i]);
			}
		}

		int count = 0, idx = 0;
		for (int i = 0; i < n; ++i) {
			if (fg.count(sum_b[i]) == 0) {
				++count;
				idx = i;
			}
		}

		if (count > 1) {
			continue;
		}

		vector<int> res;
		for (int i = 0; i < sz; ++i) {
			if (msk & (1 << i)) {
				res.push_back(a[i][idx]);
			}
		}
		sort(res.begin(), res.end());
		return res;
	}
	return vector<int>();
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> n;
		int temp = 2 * n - 1;
		for (int j = 0; j < temp; ++j) {
			a[j].resize(n);
			sum[j] = 0;
			for (int k = 0; k < n; ++k) {
				cin >> a[j][k];
				sum[j] += a[j][k];
			}
		}
		cout << "Case #" << i << ":";
		vector<int> sol = solve();
		for (int j = 0; j < sol.size(); ++j) {
			cout << " " << sol[j];
		}
		cout << endl;
	}
	return 0;
}