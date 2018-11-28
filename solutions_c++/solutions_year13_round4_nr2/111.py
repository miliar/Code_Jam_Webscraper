#pragma comment(linker, "/STACK:128777216")

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <functional>
#include <numeric>
#include <sstream>
#include <exception>
#include <cassert>

typedef long long i64;
typedef unsigned int u32;
const int null = 0;

using namespace std;

template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T abs(const T &a) {
	return (a < 0? -a: a);
}
template<class T> T sqr(const T &a) {
	return a * a;
}

#define all(a) a.begin(),a.end()

int get_best_place(i64 m, int r) {
	i64 place = 0;
	m--;
	for (int i = 0; i < r; i++) {
		if (m <= 0) {
			place += place + 1;
		} else {
			place += place;
			m--;
			m /= 2;
		}
	}
	return place;
}

int get_worst_place(i64 m, int r) {
	i64 place = 0;
	m--;
	for (int i = 0; i < r; i++) {
		if (m <= 0) {
			place += place;
		} else {
			place += place + 1;
			m--;
			m /= 2;
		}
	}
	return place;
}

int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	//freopen("input.txt", "w", stdout);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int iTest = 1; iTest <= T; iTest++) {
		i64 n, p;
		int r;
		scanf("%d %lld", &r, &p);
		n = 1LL << r;
		int r1 = 0, r2 = 0;
		for (i64 i = 0; i < n; i++) {
			if (get_best_place(n - i, r) < p) {
				r2 = i;
			}
			if (get_worst_place(i + 1, r) < p) {
				r1 = i;
			}
		}
		printf("Case #%d: %d %d\n", iTest, r1, r2);
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}