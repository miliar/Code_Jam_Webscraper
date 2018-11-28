#include <iostream> 
#include <stdlib.h>
#include <math.h>

using namespace std;
long long v[11];
int n;
void getNext(int* a) {
	a[0] += 1;
	for (int i = 0; i < n; i++) {
		if (a[i] == 2) {
			++a[i+1];
			a[i] = 0;
		}
	}
	if (a[0] == 0) {
		++a[0];
	}
}

bool isNotPrime(long long x, long long k) {
	// cout << x << endl;
	for (int i = 2; i <= (int)sqrt(x); i++) {
		if (x % i == 0) {
			v[k] = i;
			return true;
		}
	}
	return false;
}

bool isGood(int* a) {
	for (long long k = 2; k <= 10; k++) {
		long long x = 0;
		for (int i = n-1; i>=0; i--) {
			x = x * k + a[i];
		}
		if (!isNotPrime(x, k)) {
			// cout << "false" << endl;
			return false;
		}
	}
	return true;
}

int main() {
	int t;
	cin >> t;

	int j;
	cin >> n >> j;

	cout << "Case #1:" << endl;
	long long x;
	int c = 0;
	int a[35];
	for (int i = 0; i < n; i++) {
		a[i] = 0;
	}

	a[n-1] = 1;

	while (c < j) {
		getNext(a);
		if (isGood(a)) {
			for (int i = n-1; i >=0; i--) {
				cout << a[i];
			}
			for (int i = 2; i <= 10; i++) {
				cout << " " << v[i];
			}
			cout << endl;
			++c;
		}
	}

	return 0;
}