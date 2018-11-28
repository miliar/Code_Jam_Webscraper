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
#include <windows.h>

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

const int max_n = 20;

char s[max_n + 2];
double dp[1 << max_n];
double p[1 << max_n];

int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	//freopen("input.txt", "w", stdout);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int iTest = 1; iTest <= T; iTest++) {
		scanf("%s", s);
		int n = strlen(s);
		int mask = 0;
		for (int i = 0; i < n; i++) {
			if (s[i] == 'X') {
				mask |= (1 << i);
			}
		}
		memset(dp, 0, sizeof(dp));
		memset(p, 0, sizeof(p));
		dp[mask] = 0;
		p[mask] = 1;

		for (int i = mask; i < (1 << n); i = (i + 1) | mask) {
			int nf = n;
			for (int j = 0; j < n; j++) {
				if (i & (1 << j)) {
					nf--;
				}
			}
			if (nf == 0) {
				break;
			}
			for (int j = 0; j < n; j++) {
				int k = j;
				int t = 0;
				while (i & (1 << k)) {
					k++;
					t++;
					if (k == n) {
						k = 0;
					}
				}
				int m = i | (1 << k);
				dp[m] += dp[i] / n + (n - t) * p[i] / n;
				p[m] += p[i] / n;
			}
		}
		printf("Case #%d: %.15lf\n", iTest, dp[(1 << n) - 1]);
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}