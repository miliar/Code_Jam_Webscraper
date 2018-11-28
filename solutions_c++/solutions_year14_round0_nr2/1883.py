#include <fstream>
#include <iostream>
#include <iomanip>

using namespace std;

int main(void)
{
	ofstream fout("Output.out");
	ifstream fin("Input.in");

	int Ncase, Ncurrent, done;
	double currentTime, C, F, X, v;

	fin >> Ncase;
	for(Ncurrent = 1; Ncurrent <= Ncase; Ncurrent++)
	{
		currentTime = 0;
		done = 0;
		v = 2.0;
		fin >> C >> F >> X;
		if (C >= X)
			fout << "Case #" << Ncurrent << ": " << setiosflags(ios::fixed) << setprecision(7) << X/2 << endl;
		else
		{
			while(!done)
			{
				if ((X/(v+F)) < ((X-C)/v))
				{
					currentTime += C/v;
					v += F;
				}
				else
					done = 1;
			}
			currentTime += X/v;
			fout << "Case #" << Ncurrent << ": " << setiosflags(ios::fixed) << setprecision(7) << currentTime << endl;
		}
	}
	return 0;
}
