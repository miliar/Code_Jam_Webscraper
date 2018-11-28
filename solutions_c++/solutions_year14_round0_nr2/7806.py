#include<iostream>
#include<vector>
#include<fstream>
#include<iomanip>
#include<algorithm>
using namespace std;

int main()
{
	
	ifstream fin("B-large.in");
	ofstream fout("res.txt");
	int t = 0;
	fin >> t;
	for (int i = 1; i <= t; i++)
	{
		
		fout << "Case #" << i << ": ";
		
		double C = 0.0, F = 0.0, X = 0.0;
		fin >> C >> F >> X;

		double cookieProd = 2.0;
		double timeElapsed = 0.0;

		double requiredTimeWithCurrentCookieProd = X / cookieProd;
		double requiredAfterNewFarm = C / cookieProd + X / (cookieProd + F);
		while (requiredTimeWithCurrentCookieProd > requiredAfterNewFarm)
		{
			timeElapsed = timeElapsed + C / cookieProd;
			cookieProd += F;
			requiredTimeWithCurrentCookieProd = requiredAfterNewFarm;
			requiredAfterNewFarm = timeElapsed + C / cookieProd + X / (cookieProd + F);
		}

		fout << setprecision(7) << fixed << requiredTimeWithCurrentCookieProd;
		fout << endl;

	}
	fin.close();
	fout.close();
	
	return 0;
}
