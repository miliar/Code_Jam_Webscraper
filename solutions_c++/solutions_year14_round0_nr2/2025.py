#include <iostream>
#include <fstream>
#include <memory.h>
#include <iomanip>

using namespace std;

int T;
double C;
double F;
double X;

double calc(double speed) {
	double result = 0.0;
	result = (X/speed);
	return result;
}

double calcBuyFarm(double speed) {
	double timeFarm = 0.0;
	timeFarm = (C/speed);
	return timeFarm;
}

int main() {	
	double speed;
	double prevTime;
	double a,b;
	double minTime;
	ifstream inFile;
	ofstream outFile;
	inFile.open("B-large.in");
	outFile.open("B-large.out");

	inFile >> T;

	for(int i=0;i<T;i++){
		inFile >> C >> F >> X;
		// set to default.
		speed = 2.0;
		prevTime = 0.0;

		while (1) {
			a = calc(speed);
			b = calcBuyFarm(speed);
			if(a<b+(X/(speed+F))) {
				minTime = a + prevTime;
				break;
			} else {
				prevTime = b + prevTime;
				speed += F;
			}
		}
		
		outFile << "Case #" << i+1 << ": " ;
		outFile << fixed << setprecision(7);
		outFile << minTime << endl;
	}
	return 0;
}
