#pragma comment(linker, "/STACK:512777216")

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
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
#include <windows.h>

typedef long long i64;
typedef unsigned int u32;
const int null = 0;

using namespace std;

typedef vector<int> VI;

template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T abs(const T &a) {
	return (a < 0 ? -a : a);
}
template<class T> T sqr(const T &a) {
	return a * a;
}

#define all(a) a.begin(),a.end()

const int max_n = 1000000;
i64 a[max_n];

int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	//freopen("input.txt", "w", stdout);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int iTest = 1; iTest <= T; iTest++) {
		int n;
		i64 p, q, r, s;
		cin >> n >> p >> q >> r >> s;
		i64 sl = 0, sm = 0, sr = 0;
		for (int i = 0; i < n; i++) {
			int t = (i * p + q) % r + s;
			a[i] = t;
			sr += a[i];
		}
		i64 sum = sr;
		i64 mx = sum;

		for (int i = 0, j = 0; i < n; i++) {
			if (i == j) {
				sr -= a[j];
				sm += a[j];
				j++;
			}
			mx = min(mx, max(max(sl, sm), sr));
			while (sm < sr) {
				sr -= a[j];
				sm += a[j];
				j++;
				mx = min(mx, max(max(sl, sm), sr));
			}
			sm -= a[i];
			sl += a[i];
		}
		printf("Case #%d: %.15lf\n", iTest, (sum - mx) / double(sum));
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}