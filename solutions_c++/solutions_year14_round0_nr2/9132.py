#include <iostream>
#include <fstream>
#include <iomanip>

int main()
{
	std::ifstream myfile("B-large.in");
	std::ofstream output;
	output.open("output.txt");

	int amountOfTests = 0;
	const double iCps = 2.0f;
	
	if (myfile.is_open())
	{
		myfile >> amountOfTests;

		for (int testIndex = 0; testIndex < amountOfTests; ++testIndex)
		{
			double C, F, X;
			myfile >> C >> F >> X;
			
			double totalTime = 0;
			double cps = iCps;

			for (;;)
			{
				double projectedFinish = totalTime + (X - C) / cps;
				double projectedPlusFarm = totalTime + X / (cps + F);
				if (projectedFinish < projectedPlusFarm)
					break;
				totalTime += C / cps;
				cps += F;
			}

			totalTime += (X / cps);

			output << "Case #" << (testIndex + 1) << ": ";
			output << std::fixed << std::setprecision(7) << totalTime << std::endl;
		}

		myfile.close();
		output.close();
	}

	return 0;
}