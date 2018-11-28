#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <algorithm>
#include <iostream>
#include <utility>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <limits>
#include <stack>
#include <cmath>
#include <queue>
#include <map>
#include <set>

static inline int popcount(int x) {
    return __builtin_popcount(x);
}
 
template<class T, class U>
static inline std::pair<T, U> mp(const T& a, const U& b) {
    return std::make_pair(a, b);
}

bool check(int* digits) {
	for (int i = 0; i < 10; i++) {
		if (digits[i] == 0) {
			return false;
		}
	}

	return true;
}

long long solve(int N) {
	if (N == 0)
		return -1;

	int gao[10] = {0};
	for (int i = 1; i <= 1e6; i++) {
		long long gu = 1LL * i * N;
		long long cpy = gu;
		while (cpy > 0) {
			gao[cpy % 10]++;
			cpy /= 10;
		}

		if (check(gao)) {
			return gu;
		}
	}

	return -1;
}

#define FILE_IO 1

int main() {
	std::freopen("gu.txt", "r", stdin);
	std::freopen("gao.txt", "w", stdout);
	int tc;
	std::scanf("%d", &tc);
	for (int i = 1; i <= tc; i++) {
		int N;
		std::scanf("%d", &N);
		int sol = solve(N);
		if (sol == -1)
			std::printf("Case #%d: INSOMNIA\n", i);
		else
			std::printf("Case #%d: %d\n", i, sol);
	}

	std::fflush(stdout);
	std::system("open gao.txt");
	return 0;
}
