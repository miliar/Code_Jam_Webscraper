#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

double cookie(int curFarmNum);

double farmPrice, farmProduct, goal;

int main()
{
	ifstream inFile;
	ofstream outFile;
	int T;
	double time;
	int caseIndex;

	inFile.open("E:\\C++\\GCJ\\Google Code Jam 2014\\Qualification Round\\B Cookie Clicker Alpha\\B-small-attempt0.in");
	outFile.open("E:\\C++\\GCJ\\Google Code Jam 2014\\Qualification Round\\B Cookie Clicker Alpha\\B-small-attempt0.out");

	inFile >> T;
	for (caseIndex = 1; caseIndex <= T; caseIndex++)
	{
		inFile >> farmPrice >> farmProduct >> goal;
		time = cookie(0);

		cout.setf(ios::fixed);
		cout << setprecision(7) << "Case #" << caseIndex << ": " << time << endl;
		outFile.setf(ios::fixed);
		outFile << setprecision(7) << "Case #" << caseIndex << ": " << time << endl;
	}//for (caseIndex = 1; caseIndex <= T; caseIndex++)

	inFile.close();
	outFile.close();

	system("pause");
	return 0;
}

double cookie(int curFarmNum)
{
	double time, time1MoreFarm;
	double cookiesPS = 2 + farmProduct * curFarmNum;
	time = goal / cookiesPS;
	time1MoreFarm = farmPrice / cookiesPS + goal / (cookiesPS + farmProduct);

	return time < time1MoreFarm ? time : farmPrice / cookiesPS + cookie(curFarmNum + 1);
}