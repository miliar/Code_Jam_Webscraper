#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#include <numeric>
#include <queue>
#include <random>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ld;

#define TASK "connect"

int solve();

int main() {
#ifdef PoDuReM
	freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
#else
	//freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
#endif
	return solve();
}

const int dd = (int)1e3 + 7;
const int inf = (int)1e9 + 7;

int A[dd][dd];
char s[dd];

int solve() {
	int T;
	scanf("%d\n", &T);
	for (int it = 1; it <= T; ++it) {
		int ans = 0, k;
		scanf("%s %d\n", &s, &k);
		int n = strlen(s);
		for (int i = 0; i < n - k + 1; ++i)
			if (s[i] == '-') {
				for (int j = i; j < i + k; ++j)
					s[j] = (s[j] == '-' ? '+' : '-');
				++ans;
			}
		int ok = 1;
		for (int i = n - k + 1; i < n; ++i)
			if (s[i] == '-') ok = 0;
		if (ok) printf("Case #%d: %d\n", it, ans);
		else printf("Case #%d: IMPOSSIBLE\n", it);
	}
	return 0;
}