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

double solve() {
	double cost, produce, goal;
	cin >> cost >> produce >> goal;

	double total_time = 0.0;
	double cps = 2.0;

	while(true) {
		const double next_buy_time = cost / cps;
		const double next_cps = cps + produce;

		if(goal / cps < next_buy_time + goal / next_cps) {
			total_time += goal / cps;
			return total_time;
		}

		total_time += next_buy_time;
		cps = next_cps;
	}
}

int main() {
	cin.tie(nullptr);
	ios::sync_with_stdio(false);
	cout.precision(7);
	cout.setf(ios::fixed);

	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": " << solve() << "\n";
	}

	return EXIT_SUCCESS;
}
