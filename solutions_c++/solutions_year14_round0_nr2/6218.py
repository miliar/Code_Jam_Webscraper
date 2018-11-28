#include <iostream>
#include <fstream>

#include <iomanip> 
using namespace std;

int main()
{
	ofstream fout("B-large.out");
	ifstream fin("B-large.in");

	int t; 	fin >> t;
	fout  << setiosflags(ios::fixed | ios::showpoint) << setprecision(7);

	for (int i = 1; i <= t; i++)
	{
		double C, F, X, two = 2.0;
		fin >> C >> F >> X;
		double cOverF;
		double xOverF = X / two;
		double timeMax = xOverF;
		double totaltime = 0.0f;
		do
		{	
			cOverF = C / two;
			two += F;
			xOverF = X / two;
	
			double timeMaxIfBuyFarm = cOverF + xOverF;

			if (timeMaxIfBuyFarm < timeMax)
			{
				timeMax = xOverF;
				totaltime += cOverF;
			}
			else break;
		} while (true);
		double extratime = X / (two - F);
		fout << "Case #" << i << ": " << extratime + totaltime << endl;
	}
	fout.close();
	fin.close();
	return 0;
}
