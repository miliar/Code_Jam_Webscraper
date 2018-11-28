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

constexpr int MAX_M = 1000;

int m, n;
string words[MAX_M];

int ans;
int cnt;
int assign[MAX_M];

int cost(const vector<string> &vec) {
	vector<string> word_list;

	for(const auto &s : vec) {
		for(unsigned i = 0; i <= s.size(); ++i) {
			word_list.emplace_back(s.substr(0, i));
		}
	}

	sort(word_list.begin(), word_list.end());
	return unique(word_list.begin(), word_list.end()) - word_list.begin();
}

void calc() {
	vector<vector<string>> strings(n);
	for(int i = 0; i < m; ++i) {
		strings[assign[i]].emplace_back(words[i]);
	}

	sort(strings.begin(), strings.end());

	int tmp = 0;
	for(const auto &e : strings) {
		tmp += cost(e);
	}

	if(tmp > ans) {
		ans = tmp;
		cnt = 1;
	}
	else if(tmp == ans) {
		++cnt;
	}
}

void dfs(int idx = 0) {
	if(idx == m) return calc();

	for(int i = 0; i < n; ++i) {
		assign[idx] = i;
		dfs(idx + 1);
	}
}

string solve() {
	cin >> m >> n;

	for(int i = 0; i < m; ++i) {
		cin >> words[i];
	}

	ans = 0;

	dfs();
	return to_string(ans) + " " + to_string(cnt);
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
