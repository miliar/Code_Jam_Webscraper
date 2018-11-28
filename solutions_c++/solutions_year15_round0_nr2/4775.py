#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T = 0;
	cin >> T;

	for (int t = 0; t < T; t++) {
		int D = 0;
		cin >> D;
		vector<int> v(D);
		for (auto& p : v) {
			cin >> p;
		}

		int ans = *max_element(v.begin(), v.end());
		for (int i = ans - 1; i > 0; i--) {
			int sp = 0;
			for (auto p : v) {
				sp += p / i - (p%i == 0);
			}
			ans = min(ans, sp + i);
		}

		printf("Case #%d: %d\n", t+1, ans);
	}

	return 0;
}