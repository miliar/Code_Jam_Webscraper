#include <fstream>
#include <iomanip>
#include <iostream>
#include <ios>

double timeWithUpgrades(int num);

double cps = 2, C, F, X, minTime, nextTime;

int main()
{
    std::fstream input("B-large.in"), output("outputB.txt");
    int T, upgradeAmount = 0;

    input >> T;
    for (int x = 1; x <= T; ++x)
    {
		input >> std::setprecision(10) >> std::fixed >> C;
		input >> std::setprecision(10) >> std::fixed >> F;
		input >> std::setprecision(10) >> std::fixed >> X;

    	upgradeAmount = 0;
		minTime = timeWithUpgrades(upgradeAmount);

		while (1)
		{
			upgradeAmount++;
			nextTime = timeWithUpgrades(upgradeAmount);
			if (nextTime <= minTime)
			{
				minTime = nextTime;
			}
			else
			{
				break;
			}
		}
		output << std::setprecision(10) << std::fixed << "Case #" << x << ": " << minTime << std::endl;
    }

    return 0;
}

double timeWithUpgrades(int num)
{
	double sum = 0;

	for (int i = 0; i < num; i++)
	{
		sum += 1/(cps+i*F);
	}
	sum *= C;
	sum += X/(cps+num*F);

	return sum;
}
