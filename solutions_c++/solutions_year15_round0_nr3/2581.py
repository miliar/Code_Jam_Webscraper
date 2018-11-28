#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cassert>
using namespace std;

void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small-attempt0.out", "wt", stdout);
#endif
}

const char* S2 = "1ijki1kjjk1ikji1";
const char* S1 = "1ijk";
const int SIGN[] = {
		1, 1, 1, 1,
		1, -1, 1, -1,
		1, -1, -1, 1,
		1, 1, -1, -1
};
char SYM[256][256];
int SIG[256][256];

void init() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			int idx = i * 4 + j;
			SYM[S1[i]][S1[j]] = S2[idx];
			SIG[S1[i]][S1[j]] = SIGN[idx];
		}
	}
}

void solve() {
	/* Read. */
	int l, x; scanf("%d %d ", &l, &x);
	vector<char> v(l * x);
	for (int i = 0; i < l * x; i++) {
		if (i < l) {
			scanf("%c", &v[i]);
		} else {
			v[i] = v[i % l];
		}
	}
	int n = l * x;

	/* Dynamic. */
	vector<char> dp(n);
	vector<int> dp2(n);
	dp[n - 1] = v[n - 1];
	dp2[n - 1] = 1;
	for (int i = n - 2; i > 0; i--) {
		dp[i] = SYM[v[i]][dp[i + 1]];
		dp2[i] = dp2[i + 1] * SIG[v[i]][dp[i + 1]];
	}

	/* Calculate. */
	char c; int s = 1;
	for (int i = 0; i < n - 2; i++) {
		if (i == 0) {
			c = v[i];
		} else {
			s = s * SIG[c][v[i]];
			c = SYM[c][v[i]];
		}
		char c2; int s2 = 1;
		for (int j = i + 1; j < n - 1; j++) {
			if (j == i + 1) {
				c2 = v[j];
			} else {
				s2 = s2 * SIG[c2][v[j]];
				c2 = SYM[c2][v[j]];
			}
			char c3 = dp[j + 1];
			int s3 = dp2[j + 1];
			//cout << i << " " << j << " " << c << " " << c2 << " " << c3 << " " << s << " " << s2 << " " << s3 << endl;
			if (c == 'i' && c2 == 'j' && c3 == 'k' && s == 1 && s2 == 1 && s3 == 1) {
				printf("YES\n");
				return;
			}
		}
	}
	printf("NO\n");
}

int main() {
	openFiles();
	init();
	int n; scanf("%d ", &n);
	for (int i = 0; i < n; i++) {
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
