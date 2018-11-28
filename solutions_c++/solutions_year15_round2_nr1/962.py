#include<iostream>
using namespace std;

long long reverse(long long n) {
	long long x = 0;
	while (n) {
		x = x * 10 + n % 10;
		n /= 10;
	}
	return x;
}

int nrdigits(long long x) {
	int nr = 0;
	while (x > 0) {
		nr++;
		x /= 10;
	}
	return nr;
}

long long get(int p) {
	if (p == 0) return 1;
	long long n = 1;
	for (int i = 1; i <= p; i++) {
		n *= 10;
	}
	return n;
}


int main() {
	freopen("a-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
	int t, i, it;
	long long n, steps, rev;
	cin >> t;
	for (it = 1; it <= t; it++) {
		cin >> n;
		steps = 0;

		while (n > 9) {
			int nrd = nrdigits(n);
			int mid = (nrd + 1) / 2;
			long long nr = get(mid);
			long long comp = get(nrd) / 10;

			if (n == comp || n % 10 == 0) {
				steps++;
				n--;
			} else {
				if (n == comp + 1) {
					steps += 2;
					n -=2;
				} else {
					steps += n % nr - 1;
					n -= n % nr;
					n++;

					if (n != reverse(n)) {
						n = reverse(n);
						steps++;
					}
				}
			}
		}

		cout << "Case #" << it << ": " << steps + n << endl;
	}
	return 0;
}