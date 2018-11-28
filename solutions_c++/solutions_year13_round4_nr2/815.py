#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 50;

long long n, p;

int main() {
	int tc;
	cin >> tc;
	
	for (int tt = 1; tt <= tc; tt++) {
		cin >> n >> p;
		
		long long aa, bb;
		long long ll = 1, tmp = 0, cc = n;
		for (int i = 0; i < n; i++) {
			tmp += ll;
			if (tmp >= p)
				break;
			cc--;
			ll *= 2;
		}
		if (cc == n) {
			aa = 0;
		} else {
			ll = (1 << (n - 1));
			aa = 0;
			for (int i = n - 1; i >= cc; i--) {
				aa += ll;
				ll /= 2;
			}
		}
		

		ll = (1 << (n - 1));
		cc = 0;
		tmp = 1;
		while (1) {
			tmp += ll;
			if (tmp > p)
				break;
			if (tmp == p) {
				cc++;
				break;
			}
			cc++;
			ll /= 2;
		}

		if (cc == n) 
			bb = (1 << n) - 1;
		else {
			bb = 0;
			ll = 1;
			for (int i = 0; i < cc; i++) {
				ll *= 2;
				bb += ll;
			}
		}
		printf("Case #%d: ", tt);
		cout << bb << " " << aa << endl;
	}
}