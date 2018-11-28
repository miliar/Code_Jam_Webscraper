#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
	void solve() {
		int tcase, r, c, w;
		cin >> tcase;
		for (int tcase_idx = 1; tcase_idx <= tcase; tcase_idx++) {
			cin >> r >> c >> w;
			int a = c / w;
			int b = c % w;
			int ans = a * r + (b == 0 ? w - 1 : w);

			printf("Case #%d: %d\n", tcase_idx, ans);
		}
	}
};

int main() {
	Solution solution;
	solution.solve();
	return 0;
}
