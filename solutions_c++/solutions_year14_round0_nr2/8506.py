/*
* Google Code Jam 2014
* Qualification Round
* Adrian Dale
* B - Cookie Clicker
*/
#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int T; // No of test cases

void SolveTestCase(double C, double F, double X)
{
	//cout << "Solving for  " << C << ", " << F << ", " << X << endl;

	double cps = 2.0;
	double cookies = 0.0;
	double totalTime = 0.0;
	double prevResult = 1000000.0;

	for (int fc = 0; true; ++fc)
	{
		double timeToX = (X ) / cps;
		double timeToNextFarm = C / cps;
		double result = totalTime + timeToX;
		//cout << "Farm " << fc << " cps=" << cps << " totalTime=" << totalTime << " timeToX=" << timeToX << " tt+ttox=" << ( result ) << endl;

		if (result > prevResult && fc > 0)
		{
			cout << setprecision(7) << fixed << prevResult;
			break;
		}
		else
			prevResult = result;
		
		

		cps += F;
		totalTime += timeToNextFarm;
		cookies += timeToNextFarm*cps;

		
	}
	
}

void ReadTestCases()
{
	string line;

	getline(cin, line);
	istringstream parser(line);
	parser >> T;

	int TestNo = 1;
	while (TestNo <= T)
	{
		getline(cin, line);
		parser.str(line);
		parser.clear();
		double C, F, X;
		parser >> C >> F >> X;
		cout << "Case #" << TestNo << ": ";
		SolveTestCase(C, F, X);
		cout << endl;

		++TestNo;
	}
}

int main()
{
	ReadTestCases();
	//SolveTestCase(500, 4, 2000);
	return 0;
}
