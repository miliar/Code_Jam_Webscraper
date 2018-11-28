#include <iostream>
#include <fstream>
#include <set>
#include <vector>
using namespace std;

void main()
{
	std::ifstream ifs ("input.txt", std::ifstream::in);
	int tests;
	ifs>>tests;
	ofstream myfile;
	myfile.open ("output.txt");
	myfile.precision(7);
	myfile.setf( std::ios::fixed, std:: ios::floatfield );
	for(int i=1;i<=tests;i++)
	{
		double Cost_farm; //C
		double Frequency_additive; //F
		double X_goal; //X
		double optTime;

		ifs>>Cost_farm>>Frequency_additive>>X_goal;
		optTime = 0;
		double Frequency_total = 2.0; //Click cookie to start
		bool notOptimized = true;

		//In every step of this while, the cookies storage is always 0
		//Every step calculates if it's worth it buying a farm and
		//does the changes as if we waited and bought the farm
		while(notOptimized)
		{
			double secondsToProgress = Cost_farm/Frequency_total;
			double secondsToWin = X_goal/Frequency_total;
			double secondsToWinWithProgress = secondsToProgress + (X_goal)/(Frequency_total + Frequency_additive);
			if(secondsToWin < secondsToWinWithProgress)
			{
				notOptimized = false;
				optTime += secondsToWin;
			}
			else
			{
				optTime += secondsToProgress;
				Frequency_total += Frequency_additive;
			}
		}
		myfile << "Case #"<<(i)<<": ";
		myfile << optTime;
		myfile<<"\r\n";
	}
	ifs.close();
	myfile.close();
}