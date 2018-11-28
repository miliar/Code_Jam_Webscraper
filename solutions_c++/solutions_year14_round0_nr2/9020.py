#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <iomanip>


int main()
{
	double c; // cost of farm
	double f; // added cookies per second per farm
	double x; // how many cookies you need
	int t;
	std::ifstream inFile;
	inFile.open("B-large.in", std::ifstream::in);
	char temp[100];
	inFile.getline(temp, 100);
	t = atoi(temp);
	double outputs[t];
	for(int i = 0; i < t; i++)
	{
		double farms = 0;
		double rate = 2;
		double timeSpent = 0;
		inFile.getline(temp, 100, ' ');
		c = atof(temp);
		inFile.getline(temp, 100, ' ');
		f = atof(temp);
		inFile.getline(temp, 100);
		x = atof(temp);
		while(true)
		{
		// calculate the time with buying a farm, and without
			double timeWithout;
			double timeWith;
			timeWithout = (x) / (rate + farms * f);
			timeWith = (c / (rate + farms * f)) + (x / (rate + (farms + 1) * (f)));
			if(timeWithout <= timeWith)
			{
				timeSpent += timeWithout;
				break;
			}
			else
			{
				timeSpent += c / (rate + farms * f);
				farms++;
			}
		}
		outputs[i] = timeSpent;


	}
	std::ofstream outFile("cookieout.txt", std::ofstream::out | std::ofstream::trunc);
	for(int i = 0; i < t; i++)
	{
		outFile<<std::fixed;
		outFile<<std::setprecision(7);
		outFile<<"Case #"<<i+1<<": "<<outputs[i]<<std::endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}
