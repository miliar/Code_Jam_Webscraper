#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <cassert>
#include <climits>
using namespace std;
string S[1005];
int D[1005], N, M, val[1005], lastoccur[105], best, num;
int lcp(string &a, string &b) {
	int n = min(a.length(), b.length());
	for (int i = 0; i < n; ++i)
		if (a[i] != b[i]) return i;
	return n;
}
void go(int x) {
	if (x == M) {
		int cnt = 0;
		memset(lastoccur, -1, sizeof(lastoccur));
		for (int i = 0; i < M; ++i) {
			if (lastoccur[val[i]] != -1) {
				int mn = INT_MAX;
				for (int j = lastoccur[val[i]]; j < i; ++j)
					mn = min(mn, D[j]);
				cnt += mn;
			}
			lastoccur[val[i]] = i;
		}
		for (int i = 1; i <= N; ++i)
			if (lastoccur[i] == -1) return;
		if (cnt < best) {
			best = cnt;
			num = 0;
		}
		if (cnt == best) ++num;
		return;
	}
	for (int i = 1; i <= N; ++i) {
		val[x] = i;
		go(x + 1);
	}
}
int main() {
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn) {
		num = 0;
		best = INT_MAX;
		scanf("%d%d", &M, &N);
		int ans = 0;
		for (int i = 0; i < M; ++i) {
			cin >> S[i];
			ans += S[i].length() + 1;
		}
		sort(S, S + M);
		for (int i = 0; i < M - 1; ++i)
			D[i] = lcp(S[i], S[i + 1]) + 1;
		go(0);
		printf("Case #%d: %d %d\n", cn, ans - best, num);
	}
}

