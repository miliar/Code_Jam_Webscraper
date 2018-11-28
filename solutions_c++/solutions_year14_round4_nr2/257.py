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

int a[1024];
int b[1024];
int p[1024];
int dp[1024][1024];
void up(int &dp, int val) {
	if (dp > val) {
		dp = val;
	}
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
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		sort(b, b + n);
		for (int i = 0; i < n; i++) {
			a[i] = find(b, b + n, a[i]) - b;
		}
		for (int i = 0; i < n; i++) {
			int p = i;
			for (int j = 0; j < i; j++) {
				if (a[j] < a[i]) {
					p--;
				}
			}
			::p[a[i]] = p;
		}
		memset(dp, 127, sizeof(dp));
		int inf = dp[0][0];
		dp[0][n - 1] = 0;
		for (int i = 0; i < n; i++) {
			for (int j = n - 1; j > i; j--) {
				if (dp[i][j] == inf) continue;
				int cn = (j - i + 1);
				int c = n - cn;
				up(dp[i + 1][j], dp[i][j] + p[c]);
				up(dp[i][j - 1], dp[i][j] + cn - 1 - p[c]);
			}
		}
		int res = dp[0][0];
		for (int i = 1; i < n; i++) {
			up(res, dp[i][i]);
		}
		printf("Case #%d: %d\n", iTest, res);
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}