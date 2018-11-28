#include <bits/stdc++.h>
using namespace std;

long long T, N;
long long BITS = (1 << 10) - 1;

long long digits(long long x) {
	long long ret = 0;
	while(x) {
		ret |= 1 << (x % 10);
		x /= 10;
	}
	return ret;
}

int main() {
	if(fopen("test.in","r")) {
		freopen("test.in", "r", stdin);
		freopen("test.out", "w", stdout);
	}
	cin >> T;
	for(int t=1; t<=T; ++t) {
		cin >> N;
		cout << "Case #" << t << ": ";
		if(N == 0) cout << "INSOMNIA" << '\n';
		else {
			long long x = N;
			long long bits = digits(x);
			while(bits != BITS) {
				x += N;
				bits |= digits(x);
			}
			cout << x << '\n';
		}
	}
}


