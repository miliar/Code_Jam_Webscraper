#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <iomanip>

using namespace std;

//const char inputFile[] = "B-small-attempt0.in";
const char inputFile[] = "B-large.in";
const char outputFile[] = "results.out";

const double cps = 2; // Cookies per second

double calculateTime(double C, double F, double X);

int main()
{
	ifstream input;
	input.open(inputFile);
	
	ofstream output;
	output.open(outputFile);
	
	int N;
	input >> N;
	
	for (int i = 0; i < N; i++)
	{
		double C;	// Farm cost
		double F;	// Cookies per second from farm
		double X;	// Goal
		
		input >> C;
		input >> F;
		input >> X;
		
		double result = calculateTime(C, F, X);
		
		output << std::fixed << std::setprecision(7);
		output << "Case #" << i + 1 << ": " << result << endl;
	}

	return 0;
}


double calculateTime(double farmCost, double farmGain, double goal)
{
	if (farmCost >= goal)
		return (goal / cps);
	else
	{
		double time = 0;
		double totalGain = cps;
		
		while (true)
		{
			double timeToGetFarm = (farmCost / totalGain);
			double timeToWin = (goal / totalGain);
			double timeToWin2 = (goal / (totalGain + farmGain));
			
			if (timeToWin <= timeToGetFarm + timeToWin2)
			{
				time += timeToWin;
				break;
			} 
			
			time += timeToGetFarm;
			totalGain += farmGain;	
		}
		return time;	
	}
}










