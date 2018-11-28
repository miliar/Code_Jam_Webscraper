#include <cstdio>
#include <iostream>

using namespace std;

bool is_pal(long long x)
{
	long long rot = 0;
	long long temp = x;
	while (temp) {
		rot = rot * 10 + temp % 10;
		temp /= 10;
	}
	return rot == x;
}

void solve()
{
	long long a, b;
	cin >> a >> b;
	long long x = 0;
	while (x * x < a) {
		++x;
	}
	int res = 0;
	for ( ; x * x <= b; ++x) {
		if (is_pal(x) && is_pal(x * x)) {
			// cout << x * x << endl;
			++res;
		}
	}
	cout << res << endl;
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}