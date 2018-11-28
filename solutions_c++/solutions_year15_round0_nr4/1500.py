// Smile please :)

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cctype>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <iomanip>
#include <numeric>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#ifdef KVARK
	#include "debug.h"
#else
#define dbg(...) (void(1))
#define dbg2(...) (void(1))
#define dbg3(...) (void(1))
#define dbg4(...) (void(1))
#define dbg5(...) (void(1))
#define dbgp(...) (void(1))
#define dbg_arr(...) (void(1))
#define dbg_vec(...) (void(1))
#endif
#define endl "\n"

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<vector<int> > vvi;
typedef vector<vector<pii> > vvpii;
typedef vector<vector<long long> > vvll;
typedef vector<long long> vll;
typedef long long int llint;

#define all(v) (v.begin()), (v.end())

template <typename T>
inline T sqr(const T& a) {
	return a * a;
}

template <typename T>
inline int sign(const T& a) {
	return a < 0 ? -1 : a > 0;
}

void task();

int main() {
#ifdef KVARK
	freopen("input.txt", "r", stdin);
	//freopen("debug.txt", "w", stderr);
	freopen("output.txt", "w", stdout);
#else
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#endif

	task();

#ifdef KVARK
//	my_debug::printProcessInfo();
#endif
	return 0;
}



void task(){
	ios_base::sync_with_stdio(0);
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int x, a, b;
		cin >> x >> a >> b;

		int ans = (a * b) % x > 0;

		for (int i = 1; i < x - 1; ++i) {
			int j = x - i;
			if (max(i, j) > min(a, b) || max(i, j) > max(a, b))
				ans = 1;
		}

		if (a > b)
			swap(a, b);

		int ok = 0;

		for (int mask = 0; mask < (1 << (x - 1)) && !ans; ++mask) {
			int cnt_up = 0;

			int ii = 0;
			int jj = 0;
			for (int j = 0; j < (x - 1); ++j) {
				if ((mask & (1 << j)) > 0) {
					++jj;
					cnt_up += (ii);
				} else {
					++ii;
					cnt_up += (b - jj);
				}
			}
			if (jj != b - 1)
				continue;

			if (ii > a)
				continue;


			ok = 1;
			for (int di = 0; di + ii <= a; ++di) {
				if (cnt_up % x == 0)
					ok = 0;
				cnt_up += b;
			}
		}


		ans |= ok;

		cout << "Case #" << test + 1 << ": ";
		if (ans) {
			cout << "RICHARD\n";
		} else {
			cout << "GABRIEL\n";
		}

	}
}
