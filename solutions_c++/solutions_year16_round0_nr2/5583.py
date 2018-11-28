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
#include <tuple>
#include <map>
#include <set>

static inline int popcount(int x) {
    return __builtin_popcount(x);
}
 
template<class T, class U>
static inline std::pair<T, U> mp(const T& a, const U& b) {
    return std::make_pair(a, b);
}

typedef std::tuple<double, double, double, double> distances;
typedef std::tuple<int, int, int> point;

int main() {
	std::freopen("gu.txt", "r", stdin);
	std::freopen("gao.txt", "w", stdout);
	int tc;
	std::scanf("%d", &tc);
	for (int i = 1; i <= tc; i++) {
		std::string S;
		std::cin >> S;
		int answer = 0;
		for (int j = 0; j + 1 < S.size(); j++) {
			if (S[j] != S[j + 1]) {
				answer++;
			}
		}

		answer += S.back() == '-';
		std::printf("Case #%d: %d\n", i, answer);
	}

	std::fflush(stdout);
	std::system("open gao.txt");
	return 0;
}
