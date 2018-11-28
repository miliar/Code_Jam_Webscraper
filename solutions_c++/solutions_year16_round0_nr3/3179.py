//============================================================================
// Name        : q1c.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

long long divisor(long long x)
{
	if (x == 1 || x == 2) {
		return 1;
	}

	long long s = (long long)sqrt(x);
	for (long long i = 2; i < s; i++) {
		if (x % i == 0) {
			return i;
		}
	}
	return 1;
}

int main() {
	long long X[9];
	long long expo[9][32];
	long long divisorList[9];
	int T, N, J;
	int i, j, k;

	cin >> T;

	// Initialize exponents
	for (int i = 2; i <= 10; i++ ) {
		expo[i - 2][0] = 1;
		for (j = 1; j < 32; j++) {
			expo[i-2][j] = expo[i-2][j - 1]*i;
		}
	}

	for (int index = 0; index < T; index++) {
		cout << "Case #" << index+1 << ":" << endl;
		cin >> N >> J;

		// Enumerate the numbers
		bool digits[32];
		for (i = 0; i < N-2; i++) {
			digits[i] = false;
		}

		int jamCoinCount = 0;
		while (1) {
			// Check X[] sequence for all bases from 2 to 10
			for (i = 2; i <= 10; i++) {
				X[i-2] = expo[i-2][0] + expo[i-2][N-1];
				for (j = 0; j < N-2; j++) {
					if (digits[j]) {
						X[i-2] += expo[i-2][j+1];
					}
				}
				// check divisor
				divisorList[i-2] = divisor(X[i-2]);
				if (divisorList[i-2] == 1) {
					break;
				}
			}

			if (i > 10) {
				// Got a valid number. Print it.
				cout << "1";
				for (k = N-3; k >=0; k--) {
					cout << (digits[k]? "1" : "0");
				}
				cout << "1";
				for (j = 2; j <= 10; j++ ) {
					cout << " " << divisorList[j-2];
				}
				cout << endl;

				jamCoinCount++;
				if (jamCoinCount == J) {
					break;
				}
			}

			// Move on to next number
			for (i = 0; digits[i] && i < N-2; i++);
			if (i == N - 2) {
				break;
			}
			digits[i] = true;
			for (k = i-1; k >= 0; k--) {
				digits[k] = false;
			}
		}
	}
	return 0;
}
