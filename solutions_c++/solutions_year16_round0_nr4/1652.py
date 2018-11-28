#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

void fastInOut();

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	fastInOut();
	int t;
	ll k, c, s;
	cin >> t;
	for (int tst = 1; tst <= t; ++tst) {
		cin >> k >> c >> s;
		ll pw = 1, tot;
		for (int i = 1; i < c; ++i)
			pw *= k;
		tot = 1, cout << "Case #" << tst << ":";
		for (int i = 0; i < s; ++i)
			cout << " " << tot, tot += pw;
		cout << "\n";
	}
	return 0;
}

void fastInOut() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL), cout.tie(NULL);
}
