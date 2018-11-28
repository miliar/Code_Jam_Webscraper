#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 1010;

int a[MAXN];

int main() {
	int tt;
	cin >> tt;
	for (int o = 1; o <= tt; o++) {
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		int ans = MAXN;
		for (int step = 0; step < MAXN; step++) {
			int lo = 0, hi = MAXN;
			while (hi - lo > 1) {
				int mid = (lo + hi) >> 1;
				int cnt = 0;
				for (int i = 0; i < n; i++)
					cnt += (a[i] + mid - 1) / mid - 1;
				if (cnt <= step)
					hi = mid;
				else
					lo = mid;
			}
			ans = min(ans, step + hi);
		}
		cout << "Case #" << o << ": " << ans << endl;
	}
	return 0;
}
