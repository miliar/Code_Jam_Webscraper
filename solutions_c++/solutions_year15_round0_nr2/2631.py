#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <iomanip>
#include <utility>
#include <functional>


// [have][min split]
int dp[1011][1011];

using namespace std;

int main() {
	// base case
	for (int i = 0; i <= 1000; i++) {
		for (int j = i; j < 1000; j++) {
			dp[i][j] = 0;
		}
	}
	// recur
	for (int i = 1; i <= 1000; i++) {
		for (int j = 1; j < i; j++) {
			int m = 1 << 30;
			for (int k = 1; k < i; k++) {
				m = min(dp[k][j] + dp[i - k][j] + 1, m);
			}
			dp[i][j] = m;
		}
	}

	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int D; cin >> D;
		vector<int> data;
		int k = 0;
		for (int i = 0; i < D; i++) {
			int P; cin >> P;
			k = max(k, P);
			data.push_back(P);
		}
		int best = 1 << 30;
		for (int i = 1; i <= k; i++) {
			int tot = i;
			for (int m = 0; m < data.size(); m++) {
				tot += dp[data[m]][i];
			}
			best = min(best, tot);
		}
		std::cout << "Case #" << (t) << ": " << best << endl;
	}

	return 0;
}