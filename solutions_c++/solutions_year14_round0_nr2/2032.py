#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <iterator>
#include <fstream>
#include <math.h>


void someinduistcode(std::ofstream& out, double num)
{
	int f = std::floor(num);
	out << f;
	out << ".";

	num -= f;
	for (int i = 0; i < 7 ;++i)
	{
		num *= 10;
		int f = std::floor(num);
		out << f;
		num -=f;
	}

}

void solveonecase(std::ifstream& in, std::ofstream& out, int casenumber)
{
	double C;
	double F;
	double X;

	in >> C;
	in >> F;
	in >> X;
	double cookierate = 2;

	double result = 0;

	double timefornextfarm = C / cookierate;
	double timetowin = X / cookierate;
	double nexttimetowin = X / (cookierate + F);
	bool tobuyfarm = (timefornextfarm + nexttimetowin < timetowin);

	while (tobuyfarm)
	{
		result += timefornextfarm;
		cookierate += F;
		timefornextfarm = C / cookierate;
		timetowin = nexttimetowin;
		nexttimetowin = X / (cookierate + F);
		tobuyfarm = (timefornextfarm + nexttimetowin < timetowin);
	}
	result += timetowin;

	out << "Case #" << casenumber << ": ";
	someinduistcode(out, result);
	out << "\n";
}


void main(void)
{
	std::ifstream in("B-large.in");
	std::ofstream out("B-large.out");
	

	int n;
	in >> n;

	for (int i = 0; i < n; ++i)
	{
		solveonecase(in, out, i + 1);
	}
//	std::cout << "ggg";
	
//	std::system("pause");
}