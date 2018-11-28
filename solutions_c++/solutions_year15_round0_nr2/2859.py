#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int solve(const vector<int> &a)
{
	int end = *max_element(a.begin(), a.end());
	int best = 1000;
	for (int i = 1; i <= end; i++) {
		int count = 0;
		for (int j = 0; j < a.size(); j++) {
			int overflow = a[j] - i;
			if (overflow > 0) {
				count += (overflow + i - 1) / i;
			}
		}
		best = min(best, count+i);
	}
	return best;
}

int main()
{
	int T; cin >> T;
	vector<int> prob;
	prob.reserve(1001);
	for (int t=1; t<=T; t++) {
		int D; cin >> D;
		prob.clear();
		for (int i = 0; i < D; i++) {
			int tmp; cin >> tmp;
			prob.push_back(tmp);
		}
		int ans = solve(prob);
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}