#include <iostream>
#include <iomanip>

int main(int argc, char* argv[])
{
	int numCases;
	std::cin >> numCases;
	for (int i=0; i<numCases; i++)
	{
		double C, F, X;
		//C cost of a new farm
		//F farm production
		//X wining limit
		std::cin >> C >> F >> X;

		bool buildFarm = true;
		double totalTime = 0.0;
		double rate = 2.0;

		while (buildFarm)
		{
			double timeToWin = X/rate;
			double timeWithOneMoreFarm = C/rate + X/(rate+F);
			if (timeToWin <= timeWithOneMoreFarm)
			{
				totalTime += timeToWin;
				buildFarm = false;
			}
			else
			{
				totalTime += C/rate;
				rate +=F;
			}
		}
		std::cout << std::setprecision(7) << std::fixed;
		std::cout << "Case #" << (i+1) << ": " << totalTime << std::endl;
	}
	return 0;
}
