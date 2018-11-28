#include <iostream>
#include <string>
#include <sstream>

using namespace std;

void printcase(int i) {
	cout << "Case #" << i+1 << ": ";
}

void update(int A[], unsigned long N) {
	while (N > 0) {
		int digit = N % 10;
		A[digit] = 0;
		N /= 10;
	}
}

unsigned long foo(unsigned long N) {
	unsigned long n = N;
	int A[10] = {1,1,1,1,1,1,1,1,1,1};
	bool finished = false;
	while (!finished) {
		update(A, n);
		n += N;
		finished = true;
		for (int i = 0; i < 10; ++i) {
			if (A[i]) {
				finished = false;
				break;
			}
		}
	}
	n -= N;
	return n;
}

int main() {
	int T;
	unsigned long N;
	unsigned long ans;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cin >> N;
		printcase(i);
		if (N == 0)
			cout << "INSOMNIA" << endl;
		else {
			ans = foo(N);
			cout << ans << endl;
		}
	}
	return 0;
}