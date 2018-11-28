#include <iostream>
#include <conio.h>
#include <math.h>
#include <fstream>
#include <iomanip>
using namespace std;

int main() {

	ifstream readFile;
	int cases;
	readFile.open("B-large.in");
	ofstream writeFile;
	writeFile.open("p2_large_output.txt");
	writeFile << std::setprecision(7) << std::fixed;
	readFile >> cases;
	for (int i=1; i <= cases; i++) {
		double x, f, c;
		readFile >> c; readFile >> f; readFile >> x;
		double rate=2.0, timeToFarm=0.0, tillNow = 0.0, timeToBuyNow=0.0, farmAndBuyTime=0.0, previousFarmAndBuyTime = 0.0;
		farmAndBuyTime = x/rate;
		
		do {
			timeToFarm = c/rate;
			timeToBuyNow = x/rate;
			previousFarmAndBuyTime = farmAndBuyTime;
			farmAndBuyTime = tillNow + timeToBuyNow;
			tillNow += timeToFarm;
			rate += f;
		}
		while (previousFarmAndBuyTime >= farmAndBuyTime);
	
		writeFile << "Case #" << i << ": " << previousFarmAndBuyTime << endl;	
	}
	return 0;
}
