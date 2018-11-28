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

const int maxa = 1000;

std::vector<int> aa, bb, kk, ans;

int main() {
	assert(fin && fout);
	std::ios_base::sync_with_stdio(false);

	int testCnt;
	fin >> testCnt;
	aa.reserve(testCnt);
	bb.reserve(testCnt);
	kk.reserve(testCnt);
	ans.resize(testCnt);

	for (int testIdx = 1; testIdx <= testCnt; ++testIdx) {
		int a, b, k;
		fin >> a >> b >> k;
		aa.push_back(a);
		bb.push_back(b);
		kk.push_back(k);
	}

	for (int i = 0; i <= maxa; ++i) {
		for (int j = 0; j <= maxa; ++j) {
			int t = i & j;
			for (int testIdx = 0; testIdx < testCnt; ++testIdx) {
				if (i < aa[testIdx] && j < bb[testIdx] && t < kk[testIdx])
					++ans[testIdx];
			}
		}
	}

	for (int testIdx = 1; testIdx <= testCnt; ++testIdx) {
		fout << "Case #" << testIdx << ": " << ans[testIdx - 1] << '\n';
	}

	return 0;
}
