#include <iostream>

using namespace std;

long long r, t;

long long ring() {
	long long n = 1;

	long long b = (2*r - 1);
	while ( t - 2*n*n - b*n >= 0 ) {
		n++;
	}

	return n-1;
}

int main() {

	int T;
	cin >> T;
	for (int i=1; i<=T; i++) {
		cin >> r >> t;
		cout << "Case #" << i << ": " << ring() << endl;
	}
}
