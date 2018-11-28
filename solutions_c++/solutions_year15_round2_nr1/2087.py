#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <climits>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <utility>

int reverse(int n) {
	int res = 0;
	while (n) {
		res = res*10 + (n % 10);
		n /= 10;
	}
	return res;
}

int main() {
	int cases, i = 1;
	std::cin >> cases;
	int MAX = 1000001;
	std::vector<int> histo;
	for (int i = 0; i < MAX; ++i) {
		histo.push_back(i);
	}

	for (int i = 10; i < MAX; ++i) {
		int rev = reverse(i);
		if (rev < i && (int)std::log10(i) != (int)std::log10(rev))
			histo[i] = histo[i-1]+1;
		else
			histo[i] = histo[i-1]+1 < histo[rev]+1 ? histo[i-1]+1 : histo[rev]+1;
	}

	// for (int i = 0; i < MAX; ++i)
	// 	std::cout << histo[i] << std::endl;

	while (i <= cases) {
		int n;
		std::cin >> n;
		std::cout << "Case #" << i << ": " << histo[n] << std::endl;
		++i;
	}
	return 0;
}