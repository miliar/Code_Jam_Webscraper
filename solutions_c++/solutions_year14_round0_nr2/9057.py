#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;
int main()
{
	int i, test_cases;
	long double C, F, X, X_time, C_time, splittime, totaltime;
	bool Run;
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	fin >> test_cases;
	for (i = 0; i < test_cases; i++)
	{
		Run = false;
		splittime = 2;
		totaltime = 0;
		fin >> C;
		fin >> F;
		fin >> X;
		X_time = X / splittime;
		C_time = (C / splittime) + (X / (F + splittime));
		while (X_time>C_time)
		{
			Run = true;
			totaltime += C / splittime;
			splittime += F;
			X_time = X / splittime;
			C_time = (C / splittime) + (X / (F + splittime));
		}
		if (Run)
			totaltime += X_time = X / splittime;
		else
			totaltime = X / splittime;
		fout << "Case #" << i + 1 << ": " << fixed << setprecision(10) << totaltime << endl;
	}
	system("pause");
	return 0;
}