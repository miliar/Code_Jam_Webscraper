#include <bits/stdc++.h>
#define int long long
using namespace std;

int solve(int a) {
	if (a == 0)
		return -1;
	int b = 0;
	int tmar = 0;
	bool mark[10];
	for (int i = 0; i < 10; ++i)
		mark[i] = false;
	while (tmar < 10) {
		b += a;
		int c = b;
		while (c) {
			if (!mark[c % 10]) {
				mark[c % 10] = true;
				tmar ++;
			}
			c /= 10;
		}
	}
	return b;
}

main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ": ";
		int a;
		cin >> a;
		a = solve(a);
		if (a == -1)
			cout << "INSOMNIA\n";
		else
			cout << a << '\n';
	}
	return 0;
}

