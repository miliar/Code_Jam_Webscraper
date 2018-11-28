#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll k, c, s, t;

ll expo(ll x, ll y) {
	if (y == 0)
		return 1;

	ll t = expo(x, y/2);
	if (y%2 == 0)
		return t*t;
	return t*t*x;
}

void print(int a, int b) {
	if (a >= k)
		return;
	
	ll tot = 0;
	for (int i = a; i <= b; ++i)
		tot = k*tot + (i%k);

	tot++;

	assert(tot <= expo(k, c));
	assert(tot >= 0);

	cout << tot << ' ';
}

int main() {
	ifstream cin("input.txt");

	cin >> t;

	for (int i = 0; i < t; ++i) {
		cin >> k >> c >> s;
		cout << "Case #" << i+1 << ": ";
		if (s*c < k) {
			cout << "IMPOSSIBLE\n"; continue;
		}

		for (int j = 0; j < s; ++j)
			print(c*j, c*j+c-1);
		cout << "\n";
	}
}