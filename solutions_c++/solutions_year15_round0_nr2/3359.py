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
#pragma endregion
//#define IN "input.txt"
//#define OUT "output.txt"

int64 t, d, s, mx, mi;
int64 *a;

void init() {
	cin >> t;
	for (int64 i = 0; i < t; i++)
	{
		mx = T_MIN(int64);
		cin >> d;
		a = new int64[d];
		for (int64 j = 0; j < d; j++)
		{
			cin >> a[j];
			mx = max(a[j], mx);
		}
		mi = mx;
		for (int64 j = 1; j < mx; j++)
		{
			s = j;
			for (int64 k = 0; k < d; k++)
			{
				if (a[k] > j)
				{
					s += (a[k] % j == 0 ? a[k] / j - 1 : a[k] / j);
				}
			}
			mi = min(s, mi);
		}
		cout << "Case #" << i + 1 << ": " << mi << "\n";
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