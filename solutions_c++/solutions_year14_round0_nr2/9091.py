#include <iostream>
#include <fstream>
using namespace std;

std::ifstream infile("B-large.in");

int main() {
	int noOfCases;
	infile >> noOfCases;
	double C, F, X, speed;
	for (int i = 0; i < noOfCases; i++) {
		infile >> C;
		infile >> F;
		infile >> X;

		speed = 2;
		cout.setf(ios::fixed);
		cout.precision(7);
		cout << "Case #" << (i + 1) << ": ";
		if (X < C) {
			cout << (X / speed) << endl;
		} else {
			double timeToFarm = C / speed;
			double time = timeToFarm, possFin = X / speed, prevFin = possFin
					+ 1;
			while (prevFin > possFin) {
				prevFin = possFin;

				speed += F;
				timeToFarm = C / speed;
				possFin = time + X / speed;
				time += timeToFarm;

			}
			cout << prevFin << endl;
		}
	}
	return 0;
}
