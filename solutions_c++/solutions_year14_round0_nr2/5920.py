#include <fstream>
#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cmath>
using namespace std;

double solve(double C, double F, double X)
{
	double result = 0;
	int a;
	a = ceil((X*F-2*C)/(C*F)-1);
	for(int i=0; i < a; i++)
	{
		result += C/(2+i*F);
	}
	if(a<0)
		a=0;
	result += X/(a*F+2);
	return result;
}

int main(void)
{
	std::ifstream fileIn("B-large.in");
	ofstream fileOut("output.txt");
	int caseNum;
	fileIn >> caseNum;

	for(int i=0;i<caseNum;i++)
	{
		double C,F,X;
		fileIn >> C;
		fileIn >> F;
		fileIn >> X;
		double result = solve(C,F,X) ;
		fileOut << "Case #" << i+1 << ": " << fixed << std::setprecision(7) << showpoint << result << endl;
	}

	fileIn.close();
	fileOut.close();
	return 0;
}