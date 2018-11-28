#include <iostream>
#include <iomanip>
using namespace std;

int main (void)
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t <<": ";
		
		double c, f, x;
		cin >> c;
		cin >> f;
		cin >> x;
		
		double time = 0;
		double rate = 2;
		
		while (true)
		{
			double timeToGoal = x / rate;
			double timeToFactory = c / rate;
			
			double nextRate = rate + f;
			double timeAfterFactory = timeToFactory + (x / nextRate);
			
			if (timeAfterFactory < timeToGoal)
			{
				//buy a factory
				rate = nextRate;
				time += timeToFactory;
			}
			else
			{
				//wait it out
				time += timeToGoal;
				break;
			}
		}
		
		cout << std::fixed << std::setprecision(7) << time << endl;
	}
}
