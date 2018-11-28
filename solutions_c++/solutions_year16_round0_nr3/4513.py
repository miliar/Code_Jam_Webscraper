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

static constexpr int MAXN = 110;
static int generated = 0;
static int J;
static std::unordered_map<std::string, std::vector<long long>> answers;

static long long POW[1000][1000];

bool get(std::string& curr, int gu, long long& luv) {
	long long conv = 0;
	std::string cpy = curr;
	std::reverse(cpy.begin(), cpy.end());
	for (int i = 0; i < curr.size(); i++)
		conv += 1LL * POW[gu][i] * (cpy[i] - '0');

	std::cerr << curr << ' ' << conv << std::endl;

	if (conv % 2 == 0) {
		luv = 2;
		return true;
	}

	for (long long i = 3; i * i <= conv; i += 2) {
		if (conv % i == 0) {
			luv = i;
			return true;
		}
	}

	return false;
}

void finish() {
	for (auto& itr : answers) {
		if (itr.second.empty())
			continue;

		std::cout << itr.first;
		for (long long d : itr.second)
			std::cout << ' ' << d;

		std::cout << "\n";
	}

	std::fflush(stdout);
	std::system("open gao.txt");
	std::exit(EXIT_SUCCESS); // out of here.
}


void brute(std::string curr, int N) {
	if (curr.size() == N) {
		for (int i = 2; i <= 10; i++) {
			long long luv;
			if (!get(curr, i, luv)) {
				answers[curr].clear();
				return;
			}

			answers[curr].push_back(luv);
		}

		generated++;
		if (generated == J)
			finish();

		return;
	}

	if (curr.size() + 1 != N)
		brute(curr + "0", N);
	
	brute(curr + "1", N);
}


int main() {
	std::freopen("gu.txt", "r", stdin);
	std::freopen("gao.txt", "w", stdout);
	int N;
	std::cin >> N;
	std::cin >> N;
	std::cin >> J;
	std::cout << "Case #1:\n";
	for (int i = 2; i <= 10; i++) {
		POW[i][0] = 1;
		for (int j = 1; j <= 16; j++) {
			POW[i][j] = POW[i][j - 1] * i;
		}
	}

	brute("1", N);
	puts("failed to solve");
	return 0;
}
