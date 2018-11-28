#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int nCases;

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	
	fin >> nCases;
	for (int i = 1; i <= nCases; i ++) {
		double iCost, iRate, iFarmRate, iGoal;
		fin >> iCost >> iFarmRate >> iGoal;
		iRate = 2;
		double dTime = 0;
		while (iGoal / iRate > iCost / iRate + iGoal / (iRate + iFarmRate)) {
			dTime += iCost / iRate;
			iRate += iFarmRate;
		}
		dTime += (float)iGoal / iRate;
		
		fout << "Case #" << i << ": " << setprecision(15) << dTime << endl;
	}
	
	return 0;
}
