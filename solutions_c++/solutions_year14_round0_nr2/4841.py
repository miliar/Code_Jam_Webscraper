//============================================================================
// Name        : CookieClickerAlpha.cpp
// Author      : Xuanchen Tang
// Version     :
// Copyright   : 
// Description : Google Code Jam, Qualification Round 2014, Problem B. Cookie Clicker Alpha
//============================================================================

#include <iostream>
#include <algorithm>
using namespace std;

double leastTime(double C, double F, double X, double speed) {
	if ((X / speed) <= (C / speed) + X / (speed + F)) {
		return X / speed;
	} else {
		return C / speed + leastTime(C, F, X, speed + F);
	}
}

int main() {
	int caseNumber;
	cin >> caseNumber;

	int i;
	double C, F, X;
	double result;

	cout.precision(7);
	cout << fixed;
	for (i = 0; i < caseNumber; ++i) {
		cin >> C >> F >> X;
		result = leastTime(C, F, X, 2.0f);
		cout << "Case #" << i + 1 << ": " << result << endl;
	}

	return 0;
}
