#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int T, m, n;
long long X, Y;
string s[1005];
int a[1005], c[1005];

int pre(string r, string s) {
	int l = min(r.length(), s.length());
	for (int i = 0; i < l; ++i) {
		if (r[i] != s[i]) return i;
	}
	return l;
}

void dfs(int z) {
	if (z == m) {
		for (int i = 0; i < n; ++i) {
			if (c[i] == 0) return;
		}
		long long x = 0;
		for (int i = 0; i < n; ++i) {
			int last = -1;
			for (int j = 0; j < m; ++j) {
				if (a[j] == i) {
					if (last == -1) {
						x += s[j].length();
					}
					else {
						x += s[j].length() - pre(s[last], s[j]);
					}
					last = j;
				}
			}
		}
		if (x == X) {
			Y++;
		}
		else if (x > X) {
			X = x;
			Y = 1;
		}
	}
	else {
		for (int i = 0; i < n; ++i) {
			a[z] = i;
			c[i]++;
			dfs(z + 1);
			c[i]--;
		}
	}
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; ++i) {
			cin >> s[i];
		}
		sort(s, s+m);
		X = -1;
		Y = -1;
		memset(a, 0, sizeof a);
		memset(c, 0, sizeof c);
		dfs(0);
		printf("Case #%d: %lld %lld\n", tc, X + n, Y);
	}
	return 0;
}