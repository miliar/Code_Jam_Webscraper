#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int l0 = 0; l0 < t; l0++) {
		int d, maxi = 0;
		cin >> d;
		vector<int> vec(1001, 0);
		for (int l1 = 0; l1 < d; l1++) {
			int i;
			cin >> i;
			vec[i]++;
			if (i > maxi) {
				maxi = i;
			}
		}

		int best = 1000;
		for (int l1 = maxi; l1 > 0; l1--) {
			int cur = 0;
			for (int l2 = 1; l2 <= maxi; l2++) {
				cur += vec[l2] * (ceil(l2 / (float)l1) - 1);
			}
			if (cur + l1 < best) {
				best = cur + l1;
			}
		}

		cout << "Case #" << l0 + 1 << ": " << best << endl;
	}
	return 0;
}
