//#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>

using namespace std;

//#define SMALL
#define LARGE

int get(char c) { return c - '0'; }

int main() {
#ifdef SMALL
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t, n;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		cout << "Case #" << tt << ": ";
		int sum = 0, ans = 0;
		string s;
		cin >> n >> s;
		for (int i = 0; i <= n; i++) {
			if (i > sum && s[i] != '0')
				ans += i - sum, sum = i;
			sum += get(s[i]);
		}
		cout << ans << endl;
	}
}