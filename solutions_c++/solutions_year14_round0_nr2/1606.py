#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

void main()
{
	ifstream inputFile("B-large.in");
	ofstream outputFile("output.txt");
	int T;
	double C, F, X, totalTime;
	double rateOfCookies;

	inputFile >> T;

	for(int i = 0; i < T; i++)
	{
		rateOfCookies = 2.0;
		totalTime = 0.0;

		// Get info from input file
		inputFile >> C;
		inputFile >> F;
		inputFile >> X;

		// Play with the info
		do
		{
			double timeToWin = X / rateOfCookies;
			double timeToBuyFarm = C / rateOfCookies;
			double timeForNextWin = timeToBuyFarm + X / (rateOfCookies + F);

			if(timeForNextWin < timeToWin)
			{
				// Buy farm
				totalTime += timeToBuyFarm;
				rateOfCookies += F;
			}
			else
			{
				// Win
				totalTime += timeToWin;
				break;
			}
		}while(true);

		outputFile << "Case #" << i + 1 << ": " << fixed << setprecision(7) << totalTime;
		outputFile << endl;
	}

}
