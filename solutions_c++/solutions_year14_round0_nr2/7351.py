#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv)
{
	int numOfTrials = 0;

	fstream testCase;
	fstream answers;
	testCase.open("test.in", ios_base::in);
	answers.open("answers.txt", ios_base::out);
	if(testCase.is_open())
	{
		testCase >> numOfTrials;
		for (int trials = 0; trials< numOfTrials; trials++)
		{
			double CPS = 2.0;
			double farmCost = 0.0;
			double extraCPS = 0.0;
			double winTotal = 0.0;
			double timeTaken = 0.0;
			testCase >> farmCost;
			testCase >> extraCPS;
			testCase >> winTotal;
			while(true)
			{
				if(winTotal/CPS < (winTotal/(CPS+extraCPS)) + farmCost/CPS)
				{
					timeTaken += winTotal/CPS;
					answers.precision(12);
					answers << "Case #" << trials+1 << ": " << timeTaken << endl; 
					break;
				}
				else
				{
					timeTaken += farmCost/CPS;
					CPS += extraCPS;
				}
			}
		}
	}
	system("pause");
	return 0;
}