#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int getCount(vector<int>& pcs, int t) {
	int ans = t;
	for (int i = 0; i < pcs.size(); ++i) {
		ans += ceil(pcs[i] * 1.0 / t) - 1;
	}
	return ans;
}

int main() {
	int T; cin >> T;
	for (int c = 1; c <= T; ++c) {
		int D, maxPan = 0; cin >> D;
		vector<int> pcs;
		for (int i = 0; i < D; ++i) {
			int pi; cin >> pi;
			pcs.push_back(pi);
			if (pcs[i] > pcs[maxPan]) {
				maxPan = i;
			}
		}
		int res = pcs[maxPan];
		for (int i = 1; i <= pcs[maxPan]; ++i) {
			int tmp = getCount(pcs, i);
			if (res > tmp) {
				res = tmp;
			}
		}
		printf("Case #%d: %d\n", c, res);
	}
}