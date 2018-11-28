#include <fstream>
#include <iomanip>
#include <stdio.h>
using namespace std;



double solve(double c, double f, double x)
{
	double divisor = 2.0;
	double currentMin = x / 2.0;
	double currentFarmCost = c / 2.0;

	double newResult = currentMin;
	do
	{
		currentMin = newResult;
		divisor += f;
		newResult = x / divisor + currentFarmCost;
		currentFarmCost += c / divisor;
		
	} while (newResult < currentMin);

	return currentMin;
}


void main()
{
	ifstream input_file("input.txt");
	ofstream output_file("output.txt");

	int nbCases;
	input_file >> nbCases;

	for (int i = 1; i <= nbCases; ++i) {

		double c;
		input_file >> c;

		double f;
		input_file >> f;

		double x;
		input_file >> x;

		output_file << "Case #" << i << ": " << fixed << setprecision(7) << solve(c, f, x) << endl;
	}



}