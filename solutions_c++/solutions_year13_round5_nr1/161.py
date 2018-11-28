#include <iostream>
#include <cassert>
#include <algorithm>
#include <iomanip>
#include <vector>
using namespace std;

double solve() {
	int N;
	long long B;
	cin >> B >> N;
	vector<long long> X(37, 0);
	for (int i = 0; i < N; ++i) {
		cin >> X[i];
	}
	sort(X.begin(), X.end());
	X.push_back(1LL << 60);
	long long sum = 0;
	double best = 0;
	for (int i = 1; i <= 37; ++i) {
		// take numbers [0, i) up as far as possible
		sum += X[i-1];
		long long limit1 = X[i-1];
		long long limit2 = X[i];
		if (i >= 36)
			continue;
		if (limit1 == limit2)
			continue;
		// bet in [limit1, limit2) on the first i numbers

		long long sum2 = 0;
		for (int j = 1; j <= i; ++j) {
			sum2 += X[j-1];

			long long goodbet = j * (limit2-1) - sum2;
			long long actualbet = i * (limit2-1) - sum + (i - j);
			if (actualbet <= B) {
				double expected = (double)goodbet * (36.0 / j) - (double)actualbet;
				if (expected > best)
					best = expected;
			}

			goodbet = j * limit1 - sum2;
			actualbet = i * limit1 - sum + (i - j);
			if (actualbet <= B) {
				double expected = (double)goodbet * (36.0 / j) - (double)actualbet;
				if (expected > best)
					best = expected;
			}

			goodbet = j * limit1 - sum2;
			long long beteach = (B - (i - j) + sum) / i;
			if (limit1 <= beteach && beteach <= limit2-1) {
				goodbet = j * beteach - sum2;
				actualbet = i * beteach - sum + (i - j);
				if (actualbet <= B) {
					double expected = (double)goodbet * (36.0 / j) - (double)actualbet;
					if (expected > best)
						best = expected;
				}
			}
		}
	}
	return best;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
		cout << "Case #" << i << ": " << setprecision(8) << fixed << solve() << endl;
	return 0;
}
