#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>

using namespace std;

void main(){

	ifstream inFile;
	ofstream outFile;

	inFile.open("a-small.txt");
	outFile.open("out-small.txt");

	int n = 0;
	double time = 0;
	double c = 0;
	double f = 0;
	double x = 0;

	double calcTime = 0;
	
	inFile >> n;

	for (int i = 0; i < n; i++)
	{
		inFile >> c >> f >> x;

		time = x / 2.0;

		for (double j = 1.0; j < x / c; j++)
		{			
			calcTime = x / (2.0 + j * f);
			for (double k = 0; k < j; k++)
			{
				calcTime += c / (2.0 + k * f);
			}

			if (calcTime >= x / 2.0)
				break;

			if (calcTime < time)
				time = calcTime;
		}

		char buffer[20];
		sprintf_s(buffer, "%.7f", time);
		outFile << "Case #" << i + 1 << ": " << buffer << endl;
	}

	inFile.close();
	outFile.close();
}