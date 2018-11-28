#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <bitset>

using namespace std;

const int MAX_TIMES = 2000; // 125 * 9 + 1あれば 十分


long long solve(long long n) {
	if (n <= 0) {
		return -1;
	}

	bitset<10> nums(0);
	for (int i = 1; i < MAX_TIMES; i++) {
		auto m = n * i;
		while (m > 0) {
			nums[m % 10] = 1;
			m /= 10;
		}

		if (nums.all()) {
			return n * i;
		}
	}

	return -1;
}

int main() {
	int t;
	long long n;

	cin >> t;
	vector<int> ans(t, 0);

	for (int i = 0; i < t; i++) {
		cin >> n;
		ans[i] = solve(n);
	}

	for (int i = 0; i < t; i++) {
		if (ans[i] == -1) {
			printf("Case #%d: INSOMNIA\n", i + 1);
		} else {
			printf("Case #%d: %d\n", i + 1, ans[i]);
		}
	}
	return 0;
}
