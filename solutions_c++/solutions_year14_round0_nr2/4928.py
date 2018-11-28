#include <iostream>
#include <fstream>
#include <string>
using namespace std;
//calculate the revenue of farms recursively
inline double farmTimer(int farmNumber, double C, double F, double X, double produceRate){
	return (farmNumber==0 ? 0: C/(produceRate+F*(farmNumber-1))+farmTimer(farmNumber-1, C, F, X, produceRate));
}
double bestTime(double, double, double);

int main(){
	ifstream inputFile;
	const char *fileName = "B-small-attempt0.in";
	inputFile.open(fileName);//change filename to input file
	ofstream outputFile("gcj2014_answer2.txt");
	//set output precision and show point
	outputFile.precision(7);	
	outputFile.setf(ios::fixed);
	outputFile.setf(ios::showpoint);
	int caseNumber = 0;
	double C = 0.0; //farmCost
	double F = 0.0; //farmRewardRate
	double X = 0.0; //Goal

	if (inputFile.is_open() && outputFile.is_open()){
	// read the case number first
	inputFile  >> caseNumber;
		for (int i=0; i<caseNumber; ++i){
			inputFile >> C;
			inputFile >> F;
			inputFile >> X;
			//Output the case into answer file under instruction
			outputFile << "Case #" << i+1 << ": " << bestTime(C,F,X) << endl;
		}
		outputFile.close();
	}
	inputFile.close();
	return 0;
}

double bestTime(double C, double F, double X){
	int farmNumber = 0;
	double produceRate = 2.0;
	double newTime = X/produceRate;
	double bestTime = 50000.0, theBestTime = 50000.0;//10,0000 divide by 2.0
	while(newTime < bestTime){
	//find out the best number of farm, the while stops when buying a new farm slows the process
		bestTime = newTime;
		farmNumber++;
		//evaluate the new time when farm number increases
		newTime = farmTimer(farmNumber, C, F, X, produceRate) + X/(produceRate + F*farmNumber);
		// cout<<bestTime<<endl;
	}
	if (bestTime < theBestTime)
		theBestTime = bestTime;
	return theBestTime;
}