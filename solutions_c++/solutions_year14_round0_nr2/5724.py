#include <iostream>
#include <string>
#include <iomanip>
#include <fstream>
using namespace std;

int main()
{
	int caseTime = 0;
	
	ofstream fsout("result.txt");
//	double answers[100];
//	string solutions[100];
	cin>>caseTime;
	for (int times = 0;times < caseTime;times++)
	{
		double answer = 0.0;
		double C = 0.0,F = 0.0,X = 0.0;
		double cookies = 2.0;
		bool getTheShortestTime = false;
		cin>>C>>F>>X;

		answer = (X+0.00000001) / cookies;		//firstly,set the shortest time equals X/F
		int noOfFarms = 0;
		while (!getTheShortestTime)
		{
			double tempAnswer = 0.0;
			noOfFarms++;
			for (int i = 0;i < noOfFarms;i++)
			{
				tempAnswer += C/(2+F*i);
			}
			tempAnswer += X/(2+F*noOfFarms);

			if (answer >= tempAnswer)
			{
				answer = tempAnswer;
			}
			else
				getTheShortestTime = true;
		}
		char temp[10];
		itoa(times+1,temp,10);
		//cout <<setiosflags(ios::fixed);
		fsout<<"Case #"+(string)temp+": "<<fixed<<setprecision(7)<<answer<<endl;
		
	}
	return 0;
}