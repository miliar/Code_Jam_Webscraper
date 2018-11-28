#pragma comment(linker, "/STACK:66777216")

#include <cstdio>
#pragma warning(disable : 4996)
#include <algorithm>
#include <array>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <utility>
#include <functional>
#include <iostream>
#include <iomanip>
#include <ctime>
#include <cassert>
#include <queue>
#include <cmath>
#include <random>
#include <sstream>
#include <numeric>
#include <limits>
#include <chrono>
#include <type_traits>
#pragma hdrstop

#ifdef _MSC_VER
#include <intrin.h>

#define popcount(a) __popcnt(a)

#else
#define LLD "%lld"
#define LLU "%llu"
#define popcount(a) __builtin_popcount(a)
#define clz(a) __builtin_clz(a)
#define ctz(a) __builtin_ctz(a)
#endif

template<class T> 
inline bool umax(T& a, const T& b) {
	return (a < b ? a = b, true : false);
}

#ifdef _MSC_VER

#endif

namespace std {

template<typename T>
std::istream& operator>>(std::istream& in, std::vector<T>& vec) {
	for (auto& it : vec) {
		in >> it;
	}
	return in;
}

}  // namespace std

extern bool local_input;
extern bool local_output;

void input_txt() {
	if (!local_input) {
		freopen("input.txt", "r", stdin);
	}
	if (!local_output) {
		freopen("output.txt", "w", stdout);
	}
}

using namespace std;

int __;

void solve(istream& in, ostream& out) {
	input_txt();
	in >> __;
	for (int _ = 1; _ <= __; ++_) {
		std::cerr << _ << std::endl;
		out << "Case #" << _ << ": ";
		int n, k;
		in >> n >> k;
		vector<double> a(n);
		in >> a;
		double ans = 0;
		for (int mask = 0; mask < (1 << n); ++mask) {
			if (popcount(mask) != k) {
				continue;
			}
			vector<double> p;
			for (int i = 0; i < n; ++i) {
				if (mask & (1 << i)) {
					p.emplace_back(a[i]);
				}
			}
			double cur = 0;
			for (int m = 0; m < (1 << k); ++m) {
				if (popcount(m) != k / 2) {
					continue;
				}
				double prob = 1;
				for (int i = 0; i < k; ++i) {
					if (m & (1 << i)) {
						prob *= p[i];
					}
					else {
						prob *= (1 - p[i]);
					}
				}
				cur += prob;
			}
			umax(ans, cur);
		}
		out << fixed << setprecision(16) << ans << endl;
	}
}

#include <fstream>

bool local_input;
bool local_output;

int main() {
    srand(time(NULL));
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    istream& in = cin;
    local_input = false;

    ostream& out = cout;
    local_output = false;

    out << fixed << setprecision(16);
    solve(in, out);
    return 0;
}

