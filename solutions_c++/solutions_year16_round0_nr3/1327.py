#include <iostream>
#include <string>
#include <cmath>

#define ll long long

using namespace std;

ll serch_prime(ll n) {
	int len = sqrt(n) + 2;

	for (int i = 2; i < len; i++) {
		if (n % i == 0) {
			return i;
		}
	}
	return -1; 
}


ll interpret(int v, int n) {
	ll ret = 0;

	ll c = 1;

	while (v > 0) { 
		if (v & 1) {
			ret += c;
		}
		c *= n;
		v = v >> 1;
	}
	return ret;
}

string tenToTwo(int v,int n) {
	char c[n + 1];
	c[n] = 0;

	for (int i = 0; i < n;i++) {
		c[n - i - 1] = (v % 2) + '0';
		v = v / 2;
	}
	return c;
}

void solve(int n, int j) {

	ll base = 1 << (n - 1);
	base |= 1;

	ll memo[11];

	for (int count = (1 << (n -2)) - 1; count >= 0; count--) {
		int v = base | (count << 1);
		bool isOk = true;
		for (int k = 2; k <= 10 ; k++) {
			ll val = interpret(v,k);
			ll ret = serch_prime(val);
			if (ret == -1) {
				isOk = false;
				break;
			}
			memo[k] = ret;
		}
		if (isOk) {
			cout << tenToTwo(v,n);
			for (int k = 2; k <= 10; k++) {
				cout << " " << memo[k];
			}
			cout << endl;

			j--;
			if (j <= 0) {
				break;
			}
		}
	}
}


int main() {
	int T;

	cin >> T;

	for (int i = 0; i < T; i++) {
		int n,j;
		cin >> n >> j;
		cout << "Case #" << i + 1 << ": " << endl;
		solve(n,j);
	}
	return 0;
}