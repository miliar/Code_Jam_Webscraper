#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int n; scanf("%d", &n);
		vector<double> hers(n), his(n);
		for (int i = 0; i < n; ++i) scanf("%lf", &hers[i]);
		for (int i = 0; i < n; ++i) scanf("%lf", &his[i]);
		sort(begin(hers), end(hers));
		sort(begin(his), end(his));
		int y = n-1;
		for (int i = n-1; i >= 0; --i) {
			if (hers[y] > his[i]) {
				y--;
			}
		}
		y = n-1-y;

		int z = n-1;
		auto last = begin(his);
		for (int i = n-1; i >= 0; --i) {
			if (his[z] > hers[i])
				z--;
		}
		z = z + 1;
		printf("Case #%d: %d %d\n", t, y, z);
	}
}