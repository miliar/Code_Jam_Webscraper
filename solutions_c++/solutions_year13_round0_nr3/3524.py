/*
 * c.cpp
 *
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) {}

typedef unsigned long long ull;

bool isPalindrome(ull x) {
	ull y = 0, z = x;
	while (x) {
		y = y * 10 + (x % 10);
		x /= 10;
	}
	return y == z;
}

int main(void) {
	int t; cin >> t;
	forn(k, t) {
		ull a, b; cin >> a >> b;
		ull cnt = 0;
		ull x = (int) sqrt((double)a);
		while (x*x < a) ++x;
		for (; x*x <= b; ++x) {
			if (isPalindrome(x) && isPalindrome(x * x))
				++cnt;
		}
		cout << "Case #" << (k+1) << ": " << cnt << endl;
	}
	return 0;
}
