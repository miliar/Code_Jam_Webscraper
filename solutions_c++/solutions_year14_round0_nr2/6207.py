#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	long n, N;
	double C;
	double F;
	double X;
	double currentCookies;
	double currentGrowthRate;
	double timeElapsed;

	ifstream inFile("input.txt");
	ofstream outFile("output.txt");

	inFile >> N;

	outFile.precision(20);

	for (n=0; n<N; ++n)
	{
		inFile >> C;
		inFile >> F;
		inFile >> X;

		currentCookies=0.0;
		currentGrowthRate=2.0;
		timeElapsed=0.0;

		while (currentCookies < X)
		{
			double timeNeededToWin = (X - currentCookies) / currentGrowthRate;
			double timeNeededToBuy = C / currentGrowthRate;
			double timeNeededToWinWithNewFarm = timeNeededToBuy + ((X - currentCookies) / (F + currentGrowthRate));

			//cout << "B: " <<  currentCookies << " " << currentGrowthRate << " " << timeElapsed << endl;
			if (timeNeededToWinWithNewFarm < timeNeededToWin)
			{
				currentCookies=0.0; //C; //(currentGrowthRate * timeNeededToBuy);
				timeElapsed+=timeNeededToBuy;
				currentGrowthRate+=F;
			} else {
				currentCookies+=(currentGrowthRate * timeNeededToWin);  //could be more exact/explicit...
				timeElapsed+=timeNeededToWin;
			}
			//cout << "A: " << currentCookies << " " << currentGrowthRate << " " << timeElapsed << endl;
		}

		outFile << "Case #" << n+1 << ": " << timeElapsed << endl;
	}

	inFile.close();
	outFile.close();

	return 0;
}
