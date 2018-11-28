#include <cstdlib>

#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <limits>
#include <exception>

#include <cmath>
#include <cstring>
#include <cassert>
#include <ctime>

#include <string>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <deque>
#include <list>

#define ALL(container) (container).begin(), (container).end()
#define MP std::make_pair
#define SZ(x) int((x).size())

#define X first
#define Y second

typedef long long i64;
typedef unsigned long long u64;

typedef std::pair<int, int> pii;

template<typename t>
inline t sqr(const t x) {
	return x * x;
}

template<typename A, typename B>
A convert(const B &x) {
	A res;
	std::stringstream ss;
	ss << x;
	ss >> res;
	return res;
}

#define FILE_NAME "test"
std::ifstream fin(FILE_NAME ".in");
std::ofstream fout(FILE_NAME ".out");

const int inf = 100 * 100 + 5;

std::string MakeRoot(const std::string &str) {
	std::string res;
	res.reserve(str.size());

	if (!str.empty())
		res.push_back(str.front());

	for (int i = 1; i < (int)str.size(); ++i) {
		if (str[i] != str[i - 1])
			res.push_back(str[i]);
	}

	return res;
}

int CalcCommon(const std::string &x, const std::string &y) {
	const int n = x.size();
	const int m = y.size();

	std::vector<std::vector<int> > dp(m + 1, std::vector<int>(n + 1, inf));
	dp[0][0] = 0;
	for (int i = 1; i <= m; ++i) {
		for (int j = 1; j <= n; ++j) {
			if (x[j - 1] == y[i - 1])
				dp[i][j] = dp[i - 1][j - 1];
			if (j > 1 && x[j - 1] == x[j - 2])
				dp[i][j] = std::min(dp[i][j], dp[i][j - 1] + 1);
			if (i > 1 && y[i - 1] == y[i - 2])
				dp[i][j] = std::min(dp[i][j], dp[i - 1][j] + 1);
		}
	}

	return dp[m][n];
}

int main() {
	assert(fin && fout);
	std::ios_base::sync_with_stdio(false);

	int testCnt;
	fin >> testCnt;
	for (int testIdx = 1; testIdx <= testCnt; ++testIdx) {
		int n;
		fin >> n;
		assert(n == 2);
		std::string nl;
		std::getline(fin, nl);
		std::vector<std::string> strings;
		strings.reserve(n);

		std::string root;
		bool ok = true;

		for (int i = 0; i < n; ++i) {
			std::string str;
			std::getline(fin, str);
			strings.push_back(str);

			std::string nroot = MakeRoot(str);
			if (i == 0) {
				root = nroot;
			} else if (root != nroot) {
				ok = false;
			}
		}

		fout << "Case #" << testIdx << ": ";

		if (!ok) {
			fout << "Fegla Won\n";
		} else {
			/*int best = 100 * 100 + 5;
			for (int i = (int) root.size(); i <= 100; ++i) {
				int cbest = 0;
				for (int j = 0; j < (int)strings.size(); ++j)
					cbest += std::abs(i - (int)strings[j].size());

				best = std::min(best, cbest);
			}*/

			fout << CalcCommon(strings[0], strings[1]) << '\n';
		}
	}

	return 0;
}
