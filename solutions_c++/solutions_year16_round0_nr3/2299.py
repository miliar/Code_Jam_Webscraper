#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <string>
#include <climits>
#include <ctime>
#include <cassert>
#include <bitset>
#include <cstdio>

using namespace std;

#define mp make_pair
#define ll long long

ll n, t, j, st[11][101], ans[101];
string s;

ll get(ll x, ll b) {
	ll tmp = 0;
	ll o = 1;
	while (x) {
		tmp += (x % b) * o;
		o *= 10;
		x /= b;
	}
	return tmp;
}

ll del(ll x) {
	for (int j = 2; j <= sqrt((double)x); j++) {
		if (x % j == 0)
			return j;
	}
	return -1;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	for (int i = 2; i <= 10; i++)
		st[i][0] = 1;
	for (int i = 1; i <= 20; i++) {
		for (int jj = 2; jj <= 10; jj++) {
		st[jj][i] = st[jj][i - 1] * jj;
		}
	}
	cin >> t;
	for (int jj = 0; jj < t; jj++) {
		cin >> n >> j;
		cout << "Case #" << jj + 1 << ":\n";
		int tk = 0;
		for (int i = 0; i < (1 << (n - 2)); i++) {
			cerr << i << ' ' << tk << endl;
			if (tk == j)
				break;
			s = "1";
			for (int ii = n - 3; ii >= 0; ii--) {
				if ((i >> ii) & 1) {
					s += '1';
				}
				else {
					s += '0';
				}
			}
			s += '1';
			bool was = false;
			for (int z = 10; z >= 2; z--) {
				ll x = 0;
				for (int i = 0; i < s.length(); i++) {
					x += (s[i] - '0') * st[z][n - i - 1];
				}
				ll f = del(x);
				if (f == -1) {
					was = true;
				}
				ans[z] = f;
			}
			if (was)
				continue;
			cout << s << ' ';
			for (int i = 2; i <= 10; i++) {
				cout << ans[i] << ' ';
			}
			cout << endl;
			tk++;
		}
	}
	return 0;
}