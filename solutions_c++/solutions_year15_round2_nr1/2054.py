#pragma region headers/definitions
//Author: Romanov Artem
#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_WARNINGS
#pragma region headers
#ifndef _GLIBCXX_NO_ASSERT
#include <cassert>
#endif
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#if __cplusplus >= 201103L
#include <ccomplex>
#include <cfenv>
#include <cinttypes>
#include <cstdalign>
#include <cstdbool>
#include <cstdint>
#include <ctgmath>
#include <cwchar>
#include <cwctype>
#endif
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#if __cplusplus >= 201103L
#include <array>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <forward_list>
#include <future>
#include <initializer_list>
#include <mutex>
#include <random>
#include <ratio>
#include <regex>
#include <scoped_allocator>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeindex>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#endif
#pragma endregion
using namespace std;
typedef unsigned short ushort;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef long long int64;
typedef unsigned long long uint64;
#define EPS 1e-12
#define D_INF HUGE_VAL
#define D_NINF (-HUGE_VAL)
#define T_MAX(T) numeric_limits<T>::max()
#define T_MIN(T) numeric_limits<T>::min()
#define _IT ::iterator
#define _RIT ::reverse_iterator
#define _PT ::pointer
#define m_p make_pair
#pragma endregion
//#define IN "input.txt"
//#define OUT "output.txt"

vector< int64 > *g;
int64 n = 1000001;
int64 s, t;
int64 pw[20];
int64 *d, *p;
char *used;

int64 rev(int64 num) {
	vector< int64 > v;
	while (num > 0) {
		int64 kk = num % 10;
		v.push_back(kk);
		num /= 10;
	}
	int64 res = 0;
	for (int i = 0; i < v.size(); i++) {
		res += v[i] * pw[v.size() - 1 - i];
	}
	return res;
}

void bfs() {
	queue< int64 > q;
	q.push(s);
	used[s] = true;
	p[s] = -1;
	while (!q.empty()) {
		int64 v = q.front();
		q.pop();
		for (int64 i = 0; i < g[v].size(); ++i) {
			int64 to = g[v][i];
			if (!used[to]) {
				used[to] = true;
				q.push(to);
				d[to] = d[v] + 1ll;
				p[to] = v;
			}
		}
	}
}

void init() {
	pw[0] = 1;
	used = new char[n];
	d = new int64[n];
	p = new int64[n];
	g = new vector< int64 >[n];
	for (int i = 1; i < 20; i++) {
		pw[i] = 10 * pw[i - 1];
	}
	for (int64 i = 0; i <= 1000000; i++) {
		int64 rr = rev(i);
		if (i != 0) {
			g[i - 1].push_back(i);
		}
		if (rr != i) {
			g[i].push_back(rr);
		}
	}
	s = 0;
	bfs();
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int64 cur;
		cin >> cur;
		cout << "Case #" << i << ": " << d[cur] << endl;
	}
}

void build() {

}

void update() {

}

void solve() {

}

void printAns() {

}

int main() {
#pragma region I/O
	ios_base::sync_with_stdio(false);
#ifdef _DEBUG
	uint TEST_NUM = 0;
	freopen("input.txt", "r", stdin);
#define EOS !cin.eof()
#define P_DEBUG printf("\n           TEST %3d           \n-----////////////////////-----\n\n", ++TEST_NUM)
#else
#define EOS false
#define P_DEBUG
#ifdef IN
	freopen(IN, "r", stdin);
#endif
#ifdef OUT
	freopen(OUT, "w", stdout);
#endif
#endif
	cout.setf(ios::fixed);
	cout.precision(11);
#pragma endregion
	do {
		P_DEBUG;
		init();
		solve();
		printAns();
	} while (EOS);
	return 0;
}