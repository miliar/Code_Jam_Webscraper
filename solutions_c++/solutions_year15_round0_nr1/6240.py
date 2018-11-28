#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main () {
	freopen ("1.in", "r", stdin);
	freopen ("1.out", "w", stdout);
	int t;
	scanf ("%d", &t);
	for (int tt = 0; tt < t; tt++) {
		int n;
		string s;
		cin >> n >> s;
		int ans = 0;
		int cur = 0;
		for (int i = 0; i < n + 1; i++) {
			if (i > cur) {
				ans += i - cur;
				cur = i;
			}
			cur += s[i] - '0';
		}
		printf ("Case #%d: %d\n", tt + 1, ans);
	}
}

