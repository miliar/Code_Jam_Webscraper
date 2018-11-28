#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main() 
{
	ifstream inputfile;
	ofstream outputfile;
	int T,n;
	double C, F, X, rmin,rmax,time;
	
	inputfile.open("input.in");
	outputfile.open("output.out");

	//Read number of tests
	inputfile >> T;
	rmin = 2;
	for (int i = 0; i < T; i++)
	{
		//Read data for current test
		inputfile >> C >> F >> X;
		if (X>C)
		{
			//Calculate maximum rate before it is unnecessary to buy more farms
			rmax = F*(X - C) / C;
			//Calculate total number of farms
			if (rmax > rmin)
			{
				n = (int)ceil((rmax - rmin) / F);
			}
			else
			{
				n = 0;
			}
			//Calculate total time
			time = 0;
			for (int j = 0; j < n; j++)
			{
				time += C / (2 + j*F);
			}
			time += X / (2 + n*F);
		}
		else
		{
			time = X / rmin;
		}
		outputfile << "Case #" << i + 1 << ": " << fixed<<setprecision(7)<<time << '\n';
	}
	
	inputfile.close();
	outputfile.close();
	return 0;
}