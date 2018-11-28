#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <cstdlib>

using namespace std;

int solve(int n, string s) {
	int i, cur = 0;
	int ans = 0;
	cur += static_cast<int>(s[0]) - 48;
	for (i = 1; i <= n; i++) {
		if (cur < i) {
			ans += i - cur;
			cur = i;
		}
		cur += static_cast<int>(s[i]) - 48;
	}
	return ans;
}

int main() {

	freopen("A-large.in", "r", stdin);

	int i, j, tc, n;
	string s;
	scanf("%d", &tc);
	for (i = 0; i < tc; i++) {
		scanf("%d", &n);
		cin >> s;
		cout << "Case #" << i+1 << ": " << solve(n, s) << "\n";
	}

	return 0;
}