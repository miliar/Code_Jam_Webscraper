#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
	std::ifstream in("input.txt");
	std::ofstream out("output2.txt");
	int T;
	in >> T;

	for(int i = 0; i < T; ++i)
	{
		double C, F, X;
		in >> C >> F >> X;

		double totalTime = 0.0;
		double cookiesPerSecond = 2.0;
		while(true)
		{
			double timeToBuy = C / cookiesPerSecond;
			double timeToWin = X / cookiesPerSecond;
			double timeToWinAfterPurchase = timeToBuy + X / (cookiesPerSecond + F);

			if(timeToWin < timeToWinAfterPurchase)
			{
				totalTime += timeToWin;
				break;
			}
			else
			{
				totalTime += timeToBuy;
				cookiesPerSecond += F;
			}
		}

		out << fixed << setprecision(10) << "Case #" << (i + 1) << ": " << totalTime << std::endl;
	}

	return 0;
}

