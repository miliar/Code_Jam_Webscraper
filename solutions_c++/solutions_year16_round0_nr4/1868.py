#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

void show(vector<unsigned long long> &v) {
	for (auto el : v) {
		cout << el << " ";
	}
	cout << endl;
}

void solve_short(int no, int k, int c) {
	vector<unsigned long long> powers(c, 1);
	for (int i = 1; i < c; i++) {
		powers[i] = powers[i - 1] * k;
	}

	printf("Case #%d:", no);

	for (int i = 0; i < k; i++) {
		vector<unsigned long long> nums(c, i);
		auto a = inner_product(powers.begin(), powers.end(), nums.begin(), 0ULL);
		cout << " " << a + 1;
	}
	cout << endl;
}

int main() {
	int t, k, c, s;
	cin >> t;

	for (int i = 1; i <= t; i++) {
		cin >> k >> c >> s;
		if (k == s) {
			solve_short(i, k, c);
		}
	}
	return 0;
}
