#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <algorithm>

#define wrapper(i) std::cout << "Case #" << i << ": "

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int cases;
	std::cin >> cases;
	for (int test_case=1; test_case<=cases; test_case++) {
		long long A, B, K;
		std::cin >> A >> B >> K;
		long long count = A*std::min(K,B) + B*std::min(K,A) - std::min(K,B)*std::min(K,A);
		if (A > B) { int c = B; B = A; A = c; }
		for (int i=K; i<A; ++i)
			for (int j=i+1; j<B; ++j) {
				if ((i&j) < K) {
					if (j<A)
						count += 2;
					else
						++count;
				}
			}

		wrapper(test_case);
		std::cout << count << std::endl;

	}

	return 0;
}

