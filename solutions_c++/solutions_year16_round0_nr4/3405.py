#include <iostream>
#include <cstdio>
#include <vector>

long long pow(int a, int b) {
	long long p = 1;
	for (int i = 0; i < b; ++i) {
		p *= a;
	}
	return p;
}

std::vector<long long> slow_solve(int k, int c, int s) {
	long long size = pow(k, c - 1);
	long long pos = 1;
	std::vector<long long> ans;
	for (int i = 0; i < k; ++i) {
		ans.push_back(pos);
		pos += size;
	}
	return ans;
}

void print(int test, std::vector<long long>& ans) {
	printf("Case #%d: ", test);
	for (const auto& val : ans) {
		std::cout << val << " ";
	}
	std::cout << std::endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	std::cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int k, c, s;
		std::cin >> k >> c >> s;
		std::vector<long long> ans = slow_solve(k, c, s);
		print(test, ans);
	}
}