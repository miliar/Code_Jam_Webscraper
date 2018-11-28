#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<int, int> pii_;
typedef vector<pii_> vpii_;
typedef vector<int> vi_;

int solve(vi_& ds) {
	int biggest_d = *max_element(ds.begin(), ds.end());
	int best = biggest_d;
	for (int i = 2; i < biggest_d; ++i) {
		int divide_minute = 0;
		for (auto const &x : ds) divide_minute += (x - 1) / i;
		if (best > divide_minute + i) best = divide_minute + i;
	}
	return best;
}

int main() {
	int t; cin >> t;
	for (int tloop = 0; tloop < t; ++tloop) {
		int max_d; cin >> max_d;
		vi_ ds(max_d);
		for (int dloop = 0; dloop < max_d; ++dloop) cin >> ds[dloop];
		cout << "Case #" << tloop + 1 << ": " << solve(ds) << endl;
	}
}

