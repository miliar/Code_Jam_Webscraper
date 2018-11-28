#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

#define LL long long

LL N, J;
LL p[12];

LL jud(LL n) {
	if (n <= 2) return -1;
	for (LL i = 2; i * i <= n; i++) {
		if (n % i == 0)
			return i;
	}
	return -1;
}

void output(LL n) {
	LL ss[52];
	LL cnt = 0;
	while (n) {
		ss[cnt++] = n % 2;
		n /= 2;
	}
	for (LL i = N - 1; i >= 0; i--) {
		cout << ss[i];
	}
	for (LL i = 2; i <= 10; i++) {
		cout << " " << p[i];
	}
	cout << endl;
}

LL fun(LL n) {
	memset(p, 0, sizeof(p));
	for (LL i = 2; i <= 10; i++) {
		LL r = 0, q = n, c = 1;
		while (q) {
			r = r + q % 2 * c;
			c *= i;
			q /= 2;
		}
		//cout << " " << r << " ";
		p[i] = jud(r);
		if (p[i] == -1) {
			return 0;
		}
	}
	output(n);
	return 1;
}

int main() {
	//freopen("in.txt", "r", stdin);
	int T, cas = 1;
	cin >> T;
	while (T--) {
		cout << "Case #" << cas++ << ":\n";
		cin >> N >> J;
		LL tot = ((LL)1 << N) - 1;
		while (1) {
			if (fun(tot)) {
				J--;
			}
			if (J == 0) break;
			tot -= 2;
			if (tot <= ((LL)1 << (N - 1))) break;
		}
	}
	return 0;
}
