#include <iostream>
using namespace std;

long long gcd(long long a, long long b) {
	return a ? gcd(b % a, a) : b;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		long long a, b;
		char c;
		cin >> a >> c >> b;
		long long g = gcd(a, b);
		a /= g;
		b /= g;
		if (__builtin_popcount(b) == 1) {
			int x = 0;
			while ((((long long) (1)) << (x + 1)) <= a)
				x++;
			int y = 0;
			while ((((long long) (1)) << (y + 1)) <= b)
				y++;
			cout << y - x << endl;
		} else {
			cout << "impossible" << endl;
		}
	}
}
