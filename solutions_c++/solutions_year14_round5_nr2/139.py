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

const int max_n = 105, max_m = 2024;

struct Monster {
	int h, g;
	void scan() {
		scanf("%d %d", &h, &g);
	}
	int numHits(int damage) {
		return (h + damage - 1) / damage;
	}
	int remHealth(int damage) {
		return (h - 1) % damage + 1;
	}
} a[max_n];

int dp[max_n][max_m][2];

void up(int &dp, int v) {
	if (dp < v) {
		dp = v;
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
		int p, q, n;
		scanf("%d %d %d", &p, &q, &n);
		for (int i = 0; i < n; i++) {
			a[i].scan();
		}
		memset(dp, 255, sizeof(dp));
		dp[0][0][0] = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < max_m; j++) {
				for (int w = 0; w < 2; w++) {
					if (dp[i][j][w] >= 0) {
						int k = a[i].numHits(p);
						if (k <= j) {
							up(dp[i + 1][j - k][w], dp[i][j][w] + a[i].g);
						}
						if (w == 1) {
							if (a[i].h <= q) {
								up(dp[i + 1][j][0], dp[i][j][w]);
								continue;
							}
							a[i].h -= q;
						}
						int hits = a[i].numHits(q);
						up(dp[i + 1][j + hits][0], dp[i][j][w]);
						int rem = a[i].remHealth(q);
						if (rem <= p * (j + 1 + hits - 1)) {
							int numAHits = (rem + p - 1) / p - 1;
							up(dp[i + 1][j + hits - 1 - numAHits][1], dp[i][j][w] + a[i].g);
						}
						
						if (w == 1) {
							a[i].h += q;
						}
					}
				}
			}
		}
		int res = 0;
		for (int i = n, j = 0; j < max_m; j++) {
			for (int w = 0; w < 2; w++) {
				up(res, dp[i][j][w]);
			}
		}
		printf("Case #%d: %d\n", iTest, res);
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}