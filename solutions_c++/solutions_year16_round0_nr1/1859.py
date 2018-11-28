#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

int updateMask(int mask, int m) {
	while(m > 0) {
		int r = m%10;
		mask = mask | (1 << r);
		m /= 10;
	}
	return mask;
}

int solve(int n) {
	if(n == 0) return -1;
	int mask = 0;
	int k = 1;
	while(mask != ((1 << 10)-1)) {
		mask = updateMask(mask,k*n);
		++k;
	}
	return (k-1)*n;
}

int main() {
	// int best(0);
	// for(int n = 1;n <= 1000000; ++n) {
		// int s(solve(n));
		// int f(s/n);
		// if(f > best || f < 0 || s%n != 0) {
			// best = f;
			// cout << n << ": " << s << "(" << f << ")" << endl;
		// }
	// }
	// return 0;
	int T;
	cin >> T;
	for(int t = 1;t <= T; ++t) {
		int n;
		cin >> n;
		int s(solve(n));
		cout << "Case #" << t << ": ";
		if(s == -1) {
			cout << "INSOMNIA";
		} else {
			cout << s;
		}
		cout << endl;
	}
	return 0;
}