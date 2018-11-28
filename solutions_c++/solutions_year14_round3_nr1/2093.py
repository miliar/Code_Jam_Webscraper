#include <iostream>

using namespace std;

int gcd(int a, int b) {
	if (a % b == 0)
		return b;
	return gcd(b, a % b);
}

int minG(long p, long q) {
	int common = gcd(p, q);
	p /= common;
	q /= common;
	if (p == q)
		return 0;
	int ret = 0;
	while (p < q) {
		p <<= 1;
		++ret;
	}
	p -= q;
	q /= gcd(p, q);
	if (p > 0 && q % 2 == 1)
		return -1; 	
	//cout << p << ' '<< q << endl;
	int left = 0;
	while (q > 0) {
		++left;
		q >>= 1;
	}
	if (ret + left > 40)
		return -1;
	return ret;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		long long P, Q;
		char pad;
		cin >> P >> pad >> Q;
		//cout << P << ' ' << Q << endl;
		cout << "Case #" << i << ": ";
		int ret = minG(P, Q);
		if (ret == -1)
		 	cout << "impossible" << endl;
		else
			cout << ret << endl;
	}
}