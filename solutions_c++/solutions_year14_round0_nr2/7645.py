//============================================================================
// Name        : B_2014.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
using namespace std;

bool check_for_buy(double currentCookie, double nextCookie, double finalSumCookie, double limit_C);

int main() {
	int testCase;
	double C, F, X;
	double totalTime;
	double cookiePerSecond;
	cin >> testCase;
	for(int i = 1; i <= testCase; i++) {
		cin >> C >> F >> X;

		cookiePerSecond = 2;
		totalTime = 0;
		while(check_for_buy(cookiePerSecond, cookiePerSecond + F, X, C) == true) {
			totalTime += (C / cookiePerSecond);
			cookiePerSecond += F;
		}
		totalTime += (X / cookiePerSecond);

		cout << "Case #" << i << ": ";
		printf("%0.7f\n", totalTime);
	}
	return 0;
}

bool check_for_buy(double currentCookie, double nextCookie, double finalSumCookie, double limit_C) {
	double currentTime = finalSumCookie / currentCookie; // without spent a farm
	double nextTime = (finalSumCookie / nextCookie) + (limit_C / currentCookie); //with spent a farm

	if(currentTime < nextTime)
		return false;
	else
		return true;
}
