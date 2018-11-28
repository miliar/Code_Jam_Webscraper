//============================================================================
// Name        : CodeJam-2014.cpp
// Author      : Maysoun Hindawi
// Version     :
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

double buyAnotherAndCalculate(double C, double F, double X, double rate) {
	if (C > X)
		return X / rate;
	if (((C / rate) + (X / (rate + F))) < (X / rate))
		return buyAnotherAndCalculate(C, F, X, rate + F) + (C / rate);
	else
		return X / rate;
}

int main() {
	int cases;
	cin >> cases;
	double *results = new double[cases];

	for (int counter = 0; counter < cases; counter++) {
		double C;
		double F;
		double X;

		cin >> C;
		cin >> F;
		cin >> X;
		results[counter] = buyAnotherAndCalculate(C, F, X, 2.0);
	}
	cout.precision(7);
	for (int counter = 0; counter < cases; counter++) {
		cout << "Case #" << (counter + 1) << ": ";
		cout << fixed  << results[counter] << endl;
	}

	return 0;
}
