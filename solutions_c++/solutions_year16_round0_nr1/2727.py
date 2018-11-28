#include <bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)

int get_mask(long long x) {
	int res = 0;
	while (x > 0) {
		res |= 1 << (x % 10);
		x /= 10;
	}
	return res;
}

long long func(long long x) {
	if (x == 0) return -1;
	int t = 0;
	int cur_mask = 0;
	while (cur_mask != 1023) {
		++t;
		cur_mask |= get_mask(x * t);
	}
	return x * t;
}

int main() {
	// int n;
	// while (cin >> n) {
	// 	cout << func(n) << endl;
	// }
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		int t;
		cin >> t;
		int ans = func(t);
		if (ans == -1) puts("INSOMNIA"); else cout << ans << endl;
	}
	return 0;
}