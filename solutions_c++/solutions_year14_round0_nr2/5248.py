#include <stdio.h>
#include <iostream>

using namespace std;

const double findMinTime(const double C, const double F, const double X){
//	cout << endl;
	double totalTime = 0;
	double currentGrowth = 2;
	while((C/currentGrowth + X/(currentGrowth + F)) < (X/currentGrowth)){
		totalTime += C/currentGrowth;
//		cout << "CurrentGrowth: " << currentGrowth << " Total Time is: ";
//		cout << (totalTime + X/(currentGrowth + F))<< endl;
		currentGrowth += F;
	}
	totalTime += X/(currentGrowth);
	return totalTime;
}

int main(int argc, char **argv)
{
	int numTestCases;
	cin >> numTestCases;
	double C;
	double F;
	double X;
	double T[100];
	cout.precision(7);
	
	for(int currentTest = 1; currentTest <= numTestCases; currentTest++){
		cin >> C;
//		cout << fixed << C << " ";
		cin >> F;
//		cout << fixed << F << " ";
		cin >> X;
//		cout << fixed << X << " ";
		T[currentTest - 1] = findMinTime(C,F,X);
	}
		for(int i = 0; i < numTestCases; i++){
			cout << "Case #" << (i+1) << ": ";
			cout << fixed << T[i] << endl;
		}
	return 0;
}
