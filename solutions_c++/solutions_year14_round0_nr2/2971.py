#include <iostream>
#include <string>
#include <vector>
//#include <boost/multiprecision/cpp_int.hpp>
#include <math.h>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) 
	{
		double C,F,X;

		cin >> C >> F >> X;
		double currentrate = 2.0;
		double time = 0.0;


		while (X > 0)
		{
			double noactiontime = X / currentrate;

			double waitToBuyFarm = C / currentrate;
			double newrate = currentrate + F;
			double buyingtime = waitToBuyFarm + ( X / newrate );

			if (noactiontime < buyingtime)
			{
				// cout << time << " Wait at rate: " << currentrate << " for " << noactiontime << endl;
				time += noactiontime;
				X = 0;
			}
			else
			{
				// cout << time << " Waiting to buy a new farm for " << waitToBuyFarm << endl;
				time += waitToBuyFarm;
				currentrate = newrate;
				// cout << time << " Buy factory and raise rate to: " << newrate << endl;
			}
		}

		cout.precision( 15 );
		cout << "Case #" << (t+1) << ": " << time << endl;
	}
	return 0;
}


