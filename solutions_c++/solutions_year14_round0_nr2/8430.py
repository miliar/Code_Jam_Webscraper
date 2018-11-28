#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>

using namespace std;

void main()
{
	string inputFileName;
	cin>>inputFileName;
	ifstream fInput(inputFileName, ios::in);
	ofstream fOutput((inputFileName.substr(0, inputFileName.find('.'))+"-answer.txt"), ios::out);
	unsigned caseNumber;
	fInput>>caseNumber;
	double cost, upgrade, goal, current, time, rate;
	for(unsigned cases=1; cases<=caseNumber; cases++)
	{
		fInput>>cost>>upgrade>>goal;
		current=0;
		time=0;
		rate=2;
		while(true)
		{
			if(((goal-current)/rate)<=((cost-current)/rate+goal/(rate+upgrade)))
			{
				time+=(goal-current)/rate;
				break;
			}
			else
			{
				time+=(cost-current)/rate;
				rate+=upgrade;
			}
		}
		fOutput<<"Case #"<<cases<<": "<<setprecision(10)<<time<<'\n';
	}
}