#include <bits/stdc++.h>


int test() {
	int n;
	std::cin >> n;
	int res = std::numeric_limits<int>::max();

	std::vector<int> v;
	for(int i=1; i<=n; i++) {
		int x;
		std::cin >> x;
		v.push_back(x);
	}

	for(int i=1; i <= 1000; i++) {
		int tmp = i;
		for(auto x : v) tmp += (x-1)/i;
		res = std::min(res, tmp);
	}

	return res;
}

int main() {
	int t;
	std::cin >> t;
	for(int i=1; i<=t; i++) {
		std::cout << "Case #" << i << ": " << test() << std::endl;
	}
}
