#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for (int zz = 1; zz <= t; zz++) {

		int n;
		cin >> n;
		vector<int> diners;
		int max = -1;
		for (int i = 0; i < n; i++) {
			int k;
			cin >> k;
			diners.push_back(k);
			if (k > max)
				max = k;
		}
		int best = 999999;
		for (int i = 1; i <= max; i++) {
			int sum = i;
			for (int j = 0; j < (int)diners.size(); j++) {
				if (diners[j] <= i)
					continue;
				sum += (int)ceil((float)diners[j] / i) - 1;
			}
			if (sum < best)
				best = sum;
		}

		cout << "Case #" << zz << ": " << best << endl;

	}
	return 0;
}