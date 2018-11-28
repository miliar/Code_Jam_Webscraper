/*GOOGLE CODE JAM
 *ANDREW WILKENING
 *APRIL 11, 2014
 *PROBLEM B - COOKIE CLICKER ALPHA
 */

#include<fstream>
#include<iostream>
#include<iomanip>

using namespace std;

int main()
{
	double C, F, X, CpS, time, test;
	int runs, count;
	bool less;
	ifstream fin("LargeB.in");
	ofstream fout("LargeBSol.out");
	fin >> runs;
	fout << fixed << setprecision(7);
	for(int i = 1; i <= runs; i++)
	{
		fin >> C >> F >> X;
		count = 1;
		less = true;
		CpS = 2;
		time = X/CpS;
		while(less)
		{
			test = 0;
			CpS = 2;
			for(int j = 0; j < count; j++)
			{
				test += C/CpS;
				CpS += F;
			}
			test += X/CpS;
			if(test < time) time = test;
			else less = false;
			count++;
		}
		fout << "Case #" << i << ": " << time << endl;
	}
	
	return 0;
}
