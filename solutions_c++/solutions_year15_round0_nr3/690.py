#include <bits/stdc++.h> 
using namespace std;
int arr[5][5], mp[201];

inline int multiply(int a, int b) {
	return (a < 0 == b < 0 ? 1 : -1) * arr[abs(a)][abs(b)];
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	mp['1'] = 1, mp['i'] = 2, mp['j'] = 3, mp['k'] = 4;

	arr[1][1] = 1;
	arr[1][2] = 2;
	arr[1][3] = 3;
	arr[1][4] = 4;
	arr[2][1] = 1;
	arr[2][2] = -1;
	arr[2][3] = 4;
	arr[2][4] = -3;
	arr[3][1] = 3;
	arr[3][2] = -4;
	arr[3][3] = -1;
	arr[3][4] = 2;
	arr[4][1] = 4;
	arr[4][2] = 3;
	arr[4][3] = -2;
	arr[4][4] = -1;

	int t;
	cin >> t;
	for (int tst = 1; tst <= t; ++tst) {
		int l;
		long long k;
		cin >> l >> k;
		string s, ss;
		cin >> ss;
		for (int i = 1; i <= min(k, 20LL); ++i)
			s += ss;
		if (k > 20) {
			k %= 4;
			for (int i = 0; i < k; ++i)
				s += ss;
		}

		bool b = 0;
		int ind = 0, tmp = 1;
		l = s.size();
		for (; ind < l && !b; ++ind) {
			tmp = multiply(tmp, mp[s[ind]]);
			b |= (tmp == 2);
		}

		if (b) {
			b = 0, tmp = 1;
			for (; ind < l && !b; ++ind) {
				tmp = multiply(tmp, mp[s[ind]]);
				b |= (tmp == 3);
			}
		}

		if (b) {
			tmp = 1;
			for (; ind < l; ++ind)
				tmp = multiply(tmp, mp[s[ind]]);
			b = tmp == 4;
		}
		cout << "Case #" << tst << ": " << (b ? "YES\n" : "NO\n");
	}
}
