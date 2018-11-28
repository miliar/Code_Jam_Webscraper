#include <iostream>
#include <string>
#include <sstream>

using namespace std;

void printcase(int i) {
	cout << "Case #" << i+1 << ": ";
}

int f(int A[], int n) {
	if (n == 0) return 0;
	if (A[n-1] == 1) return f(A, n-1);
	for (int i = 0; i < n; ++i) {
		if (A[i] == 0)
			A[i] = 1;
		else 
			A[i] = 0;
	}
	return 1 + f(A, n-1);
}

int main() {
	int T;
	string S;
	int n;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cin >> S;
		n = S.length();
		int A[n];
		for (int j = 0; j < n; ++j) {
			if (S[j] == '+') 
				A[j] = 1;
			else
				A[j] = 0;
		}
		printcase(i);
		cout << f(A, n) << endl;
	}

	return 0;
}