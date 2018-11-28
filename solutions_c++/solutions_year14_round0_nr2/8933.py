#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	//ifstream inputReader("A-small-attempt0.in");
	//ofstream outputWriter("outputA.out");

	int T;
	cin>>T;

	for (int t = 0; t < T; t++)
	{
		double currentRate = 2;
		double costToUpdateRate, rateUpdate, target;
		double timeAnswer = 0;
		cin>>costToUpdateRate>>rateUpdate>>target;

		do
		{
			double currentTimeToReachTarget = target/currentRate;
			double timeToReachTargetAfterUpdate = costToUpdateRate/currentRate + target/(currentRate + rateUpdate);
			if(currentTimeToReachTarget <= timeToReachTargetAfterUpdate)
			{
				timeAnswer += currentTimeToReachTarget;
				break;
			}
			else
			{
				timeAnswer += costToUpdateRate/currentRate;
				currentRate += rateUpdate;
			}
		} while (true);

		
		printf("Case #%d: %0.7lf\n", (t+1), timeAnswer);
	}
	//outputWriter.close();
	return 0;
}