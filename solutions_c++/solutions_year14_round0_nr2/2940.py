// CodeJam_QR14_02.cpp : Defines the entry point for the console application.
//

#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

const double StartV=2.0;
const int PrecisionC=7;

double Solve(double C, double F, double X)
{
	double T=0, V=StartV;
	for (;C*V+C*F-X*F<0;)
	{
		T+=C/V;
		V+=F;
	}
	return T+X/V;
	return -1;
}

int main()
{
	int c;
	double C,F,X;
	fin >> c;
	fout.setf(ios::fixed,ios::floatfield);
	fout.precision(PrecisionC);
	for (int m=1;m<=c;m++)
	{
		fin >> C >> F >> X;
		fout << "Case #" << m <<  ": " << Solve(C,F,X) << "\n";
	}
	return 0;
}

