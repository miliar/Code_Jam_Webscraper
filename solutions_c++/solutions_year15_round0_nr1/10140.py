//============================================================================
// Name        : StandingOvation.cpp
// Author      : tj9sun
// Version     :
// Copyright   : Your copyright notice
// Description :
//============================================================================

#include <iostream>
#include <cmath>
using namespace std;

int digits[1001];

int standingOvation(int n) {
	int result = 0;
	int sum = digits[0];
	int need = 0;
	for (int i = 1; i < n; i++) {
		if (i != 0 && i > sum) {
			need = i - sum;
			result = result + need;
			sum = sum + digits[i] + need;
		} else {
			sum = sum + digits[i];
		}
	}

	return result;
}

int main() {
	int T;
	cin >> T;
	for (int n_case = 1; n_case <= T; n_case++) {
		int Smax, digit;
		cin >> Smax;
		cin >> digit;

		for (int n_Smax = Smax; n_Smax >= 0; n_Smax--) {
			digits[n_Smax] = digit % 10;
			digit = digit / 10;
		}

		int MINfriend = standingOvation(Smax + 1);
		printf("Case #%d: %d\n", n_case, MINfriend);
	}

	return 0;
}
