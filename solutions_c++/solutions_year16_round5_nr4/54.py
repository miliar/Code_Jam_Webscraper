/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

void solve() {
	int n, l;
	cin >> n >> l;
	string s[n], t;
	forn(i, n)
		cin >> s[i];
	cin >> t;
	forn(i, n)
		if (s[i] == t) {
			puts("IMPOSSIBLE");
			return;
		}
	forn(i, l) printf("01");
	printf("0?");
	printf("01");
	printf(" ");
	printf("0");
	forn(i, l - 1) printf("?");
	printf("0");
	printf("\n");
}

int main() {
	int n;
	ios_base::sync_with_stdio(0), cin.tie(0);
	cin >> n;
	for (int i = 1; i <= n; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}
