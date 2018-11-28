#include <iostream>

using namespace std;

long long t, n, m[1000], a, b, r;

int main ()
{
	cin >> t;
	for (long long _ = 0; _ ++< t;) {
		cin >> n;
		a = b = r = 0;
		for (long long i = 0; i < n; ++i) cin >> m[i];
		for (long long i = 1; i < n; ++i)	a += max(0ll, m[i-1] - m[i]), r = max(r, m[i-1] - m[i]);
		for (long long i = 0, c = 0; i < n; ++i) {
			b += min(r, c), c = max(c - r, 0ll);
			c = max(c, m[i]);
		}
		cout << "Case #" << _ << ": " << a << ' ' << b << '\n';
	}
}

