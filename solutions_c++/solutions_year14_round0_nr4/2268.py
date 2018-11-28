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

int play_deceitful_war(const vector<double> &Naomi, const vector<double> &Ken) {
	deque<double> rest(Ken.begin(), Ken.end());

	int res = 0;
	for(const auto &chosen_naomi : Naomi) {
		if(chosen_naomi > *rest.begin()) {
			++res;
			rest.pop_front();
		}
		else {
			rest.pop_back();
		}
	}
	return res;
}

int play_war(const vector<double> &Naomi, const vector<double> &Ken) {
	deque<double> rest(Ken.begin(), Ken.end());

	int res = 0;
	for(const auto &chosen_naomi : Naomi) {
		const auto it = lower_bound(rest.begin(), rest.end(), chosen_naomi);
		if(it == rest.end()) {
			++res;
			rest.pop_front();
		}
		else {
			rest.erase(it);
		}
	}
	return res;
}

string solve() {
	int n;
	cin >> n;

	vector<double> Naomi(n);
	vector<double> Ken(n);
	for(auto &e : Naomi) cin >> e;
	for(auto &e : Ken) cin >> e;

	sort(Naomi.begin(), Naomi.end());
	sort(Ken.begin(), Ken.end());

	ostringstream os;
	os << play_deceitful_war(Naomi, Ken);
	os << " ";
	os << play_war(Naomi, Ken);
	return os.str();
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
