#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

double GetTimeWithNewFarm(double destination, double rate, double cost, double increment)
{
	return (cost / rate) + (destination / (rate + increment));
}

double GetTimeToBuildNewFarm(double cost, double rate)
{
	return cost / rate;
}

double GetTimeWithoutNewFarm(double destination, double rate)
{
	return destination / rate;
}

double GetTotalTime(double c, double f, double x)
{
	double rate = 2.0;
	double totalTime = 0;

	double twnf, twonf, ttbnf;

	while (true)
	{
		twonf = GetTimeWithoutNewFarm(x, rate);
		twnf = GetTimeWithNewFarm(x, rate, c, f);

		if (twonf < twnf){
			totalTime += twonf;
			break;
		}

		ttbnf = GetTimeToBuildNewFarm(c, rate);
		totalTime += ttbnf;
		rate += f;
	}

	return totalTime;
}

int main()
{
	ifstream input;
	ofstream output;
	input.open("input.txt");
	output.open("output.txt");

	int testCases;
	double c, f, x;

	input >> testCases;

	for (int testCase = 1; testCase <= testCases; testCase++)
	{
		input >> c >> f >> x;
		double totalTime = GetTotalTime(c, f, x);
		output << "Case #" << testCase << ": " << fixed << setprecision(7) << totalTime << endl;
	}
	return 0;
}