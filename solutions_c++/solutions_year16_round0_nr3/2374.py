#include <bits/stdc++.h>
#define int long long
using namespace std;

int ans[11];

string to_string(int mask, int base) {
	string ans;
	while (mask) {
		ans += char('0' + (mask & 1));
		mask >>= 1;
	}
	reverse(ans.begin(), ans.end());
	return ans;
}

int to_base(int mask, int base) {
	int m = 1, ans = 0;
	while (mask) {
		ans += (mask & 1) * m;
		m *= base;
		mask >>= 1;
	}
	return ans;
}

int first_div(int x) {
	for (int i = 2; i * i <= x; ++i)
		if (x % i == 0)
			return i;
	return x;
}

bool check(int mask) {
	for (int i = 2; i <= 10; ++i) {
		int x = to_base(mask, i);
		int f = first_div(x);
		if (f == x)
			return false;
		ans[i] = f;
	}
	return true;
}

main() {
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, x;
	cin >> n;
	cout << "Case #1:\n";
	cin >> n >> x;
	for (int mask = 0; mask < (1 << n) && x; ++mask) {
		if ((mask & 1) == 0 || (mask & (1 << (n - 1))) == 0)
			continue;
		if (check(mask)) {
			cout << to_string(mask, 2) << ' ';
			for (int i = 2; i <= 10; ++i)
				cout << ans[i] << ' ';
			cout << '\n';
			x --;
		}
	}
	return 0;
}

