/*
 * Problem : 
 * Author : Hwhitetooth
 * Date : 
 * Result :
 */

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int N = 1000 + 10;
const int K = 100 + 10;
const int INF = 1100000;

int a[N], s[N];
int low[N], high[N];
int testCases, n, k;

int check(int upper) {
	int h = 0, flag = 1;
	for (int j = 0; j < k; ++j) {
		if (upper - high[j] < 0) {
			return 0;
		}
		h += upper - high[j];
	}
	if (h > k) {
		h = k;
	}
	if (s[0] <= h) {
		return 1;
	}
	return 0;
}

int main() {
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		memset(s, 0, sizeof s);
		scanf("%d%d", &n, &k);
		scanf("%d", &s[k - 1]);
		s[0] = s[k - 1];
		memset(a, 0, sizeof a);
		memset(low, 0, sizeof low);
		memset(high, 0, sizeof high);
		for (int i = k; i < n; ++i) {
			scanf("%d", &s[i]);
			a[i] = s[i] - s[i - 1] + a[i - k];
			low[i % k] = min(low[i % k], a[i]);
			high[i % k] = max(high[i % k], a[i]);
		}
		for (int i = 0; i < k; ++i) {
			s[0] += low[i];
			high[i] -= low[i];
		}
		s[0] = (s[0] % k + k) % k;
		int l = 0, r = INF, ret;
		while (l <= r) {
			int m = (l + r) / 2;
			if (check(m)) {
				ret = m;
				r = m - 1;
			}
			else {
				l = m + 1;
			}
		}
		printf("Case #%d: %d\n", _, ret);
	}
	return 0;
}