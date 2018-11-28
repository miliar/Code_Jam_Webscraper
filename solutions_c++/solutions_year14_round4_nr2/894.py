#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include <omp.h>
using namespace std;

#define dump(...) (cerr<<#__VA_ARGS__<<" = "<<(DUMP(),__VA_ARGS__).str()<<endl)

struct DUMP : ostringstream {
	template<class T> DUMP &operator,(const T &t) {
		if(this->tellp()) *this << ", ";
		*this << t;
		return *this;
	}
};

template<class T> inline void chmax(T &a, const T &b) { if(b > a) a = b; }
template<class T> inline void chmin(T &a, const T &b) { if(b < a) a = b; }

template<class T, class U>
ostream &operator<<(ostream &os, const pair<T, U> &p) {
	return os << '(' << p.first << ", " << p.second << ')';
}

template<class Tuple, unsigned Index>
void print_tuple(ostream &os, const Tuple &t) {}

template<class Tuple, unsigned Index, class Type, class... Types>
void print_tuple(ostream &os, const Tuple &t) {
	if(Index) os << ", ";
	os << get<Index>(t);
	print_tuple<Tuple, Index + 1, Types...>(os, t);
}

template<class... Types>
ostream &operator<<(ostream &os, const tuple<Types...> &t) {
	os << '(';
	print_tuple<tuple<Types...>, 0, Types...>(os, t);
	return os << ')';
}

template<class Iterator>
ostream &dump_range(ostream &, Iterator, const Iterator &);

template<class T>
ostream &operator<<(ostream &os, const vector<T> &c) {
	return dump_range(os, c.cbegin(), c.cend());
}

template<class Iterator>
ostream &dump_range(ostream &os, Iterator first, const Iterator &last) {
	os << '[';
	for(int i = 0; first != last; ++i, ++first) {
		if(i) os << ", ";
		os << *first;
	}
	return os << ']';
}

bool check(const vector<int> &a) {
	const int n = a.size();
	const int max_index = max_element(a.begin(), a.end()) - a.begin();

	for(int i = 0; i < max_index - 1; ++i) {
		if(a[i] > a[i + 1]) return false;
	}

	for(int i = max_index + 1; i < n - 1; ++i) {
		if(a[i] < a[i + 1]) return false;
	}

	return true;
}

int swap_count(vector<int> a, int l, int r, const function<bool(int, int)> &compare) {
	int res = 0;
	const int n = r - l;

	for(int i = 0; i < n - 1; ++i) {
		for(int j = 0; j < n - i - 1; ++j) {
			if(compare(a[j + l], a[j + 1 + l])) {
				++res;
				swap(a[j + l], a[j + 1 + l]);
			}
		}
	}

	return res;
}

string solve() {
	int n;
	cin >> n;

	vector<int> a(n);
	for(auto &e : a) cin >> e;

	int ans = INT_MAX;
	vector<int> order(n);
	iota(order.begin(), order.end(), 0);

	do {
		vector<int> tmp;
		tmp.reserve(n);

		for(int i = 0; i < n; ++i) {
			tmp.emplace_back(a[order[i]]);
		}

		if(!check(tmp)) continue;
		chmin(ans, swap_count(order, 0, n, greater<int>()));
	} while(next_permutation(order.begin(), order.end()));

	return to_string(ans);
}

int main() {
	cin.tie(nullptr);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": " << solve() << "\n";
	}

	return EXIT_SUCCESS;
}
