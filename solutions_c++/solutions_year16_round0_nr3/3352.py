#include <iostream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

void printcase(int i) {
	cout << "Case #" << i+1 << ": ";
}

int divisor(unsigned long n) {
	for (int d = 2; d <= sqrt(n); ++d) {
		if (n % d == 0)
			return d;
		if (d > 200000)
			return 1;
	}
	return 1;
}	

unsigned long arrayToNum(int A[], int N, int base) {
	if (N == 0) return 0;
	return A[N-1] + base * arrayToNum(A, N-1, base);
}

void addone(int A[], int N) {
	if (A[N-1] == 0) {
		A[N-1] = 1;
		return;
	} else {
		A[N-1] = 0;
		return addone(A, N-1);
	}
}

void printarray(int A[], int N) {
	for (int i = 0; i < N; ++i) {
		cout << A[i];
	}
}

void jamcoin(int N, int J) {
	int A[N];
	int i;
	int divisors[11];
	bool isvalid = true;
	unsigned long num;
	for (i = 0; i < N; ++i) {
		A[i] = 0;
	}
	A[0] = A[N-1] = 1;
	while (J > 0) {
		for (int base = 2; base <= 10; ++base) {
			num = arrayToNum(A, N, base);
			if ((divisors[base] = divisor(num)) == 1) {
				isvalid = false;
				break;
			}
		}
		if (isvalid) {
			printarray(A, N);
			cout << " ";
			for (i = 2; i < 11; ++i) {
				cout << divisors[i] << " ";
			}
			cout << endl;
			J--;
		}
		addone(A, N);
		addone(A, N);
		isvalid = true;
	}
}

int main() {
	int T, N, J;
	cin >> T;
	cin >> N >> J;
	printcase(0);
	cout << endl;
	jamcoin(N, J);
	return 0;
}

