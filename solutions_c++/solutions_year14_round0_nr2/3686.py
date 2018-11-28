#include<iostream>
#include<fstream>
#include<deque>
#include<map>
#include<iomanip>

using namespace std;

int main(int argc, char *argv[])
{
	ifstream file;
	ofstream outputFile;
	
	double C=0.0, F=0.0, X=0.0;
	int intTestCases=0;
	
	outputFile.open(argv[2]);
	file.open(argv[1]);

	if(!file.eof())
	{
		file >> intTestCases;
	}

	for(int t=0; t<intTestCases; ++t)
	{
		file >> C >> F >> X;
		
		double totalSeconds=0.0, currentRate=2.0;
		
		//cout << endl << C << " " << F << " " << X;
		if (X<=C) {
			totalSeconds = X/2;
		} else {
			
			while (X/currentRate > (C/currentRate + X/(F+currentRate))) {
				totalSeconds = totalSeconds + (C/currentRate);
				currentRate = currentRate + F;
			}
			
			totalSeconds = totalSeconds + X/currentRate;
	
		}

		if (t==0) {
			outputFile << "Case #" << t+1 << ": " << std::fixed << std::setprecision(7) << totalSeconds;
		}else {
			outputFile << "\nCase #" << t+1 << ": " << std::fixed << std::setprecision(7) << totalSeconds;
		}

	}
}