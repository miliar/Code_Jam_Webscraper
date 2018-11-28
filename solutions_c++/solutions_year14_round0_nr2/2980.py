#include <fstream>
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
	ifstream ifs("C:/yoshiko/programming/gcj/2014/QR/B/B-large.in");
	ofstream ofs("C:/yoshiko/programming/gcj/2014/QR/B/B-large.out");
	string line;

	getline(ifs, line);
	int nCases = 0;
	sscanf(line.c_str(), "%d", &nCases);

	cout << "cases:" << nCases << endl;

	for(int i=0; i<nCases; ++i)
	{
		getline(ifs, line);
		double C = 0.0;
		double F = 0.0;
		double X = 0.0;
		sscanf(line.c_str(), "%lf %lf %lf", &C, &F, &X);

		int nFarm = 1;
		double answer = 0;

		double fIncome = 2.0;
		double fTimeToGoal = X / fIncome;
		double fTimeToGetPrevFarm = 0.0;

	    while(true)
		{
			double fIncomeWithAdditionalFarm = fIncome + F;
			double fTimeToGoalWithAdditionalFarm = X / fIncomeWithAdditionalFarm;
			double fTimeToGetFarm = fTimeToGetPrevFarm + C / fIncome;

			if(fTimeToGetPrevFarm + fTimeToGoal < fTimeToGetFarm + fTimeToGoalWithAdditionalFarm)
			{
				answer = fTimeToGetPrevFarm + fTimeToGoal;
				break;
			}
			else
			{
				nFarm++;
				fIncome = fIncomeWithAdditionalFarm;
				fTimeToGoal = fTimeToGoalWithAdditionalFarm;
				fTimeToGetPrevFarm = fTimeToGetFarm;
			}
		}


		ofs << fixed << setprecision(7);
		ofs << "Case #" << i+1 << ": " << answer << endl;
		cout << fixed << setprecision(7);
		cout << "Case #" << i+1 << ": " << answer << endl;
	}
}