#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <iomanip>
#include <fstream>

std::ifstream in("input.in");
std::ofstream out("output.txt");

struct data
{
	double c;
	double f;
	double x;
};

void printMin(data& d)
{
	double c = d.c;
	double f = d.f;
	double x = d.x;

	double total = 0;
	double current = 2;
	while (true)
	{
		double t1 = x/current;
		double t0 = c/current;
		double t2 = t0 + x/(current+f);
		if (t2 < t1)
		{
			total += t0;
			current += f;
		}
		else
		{
			total += t1;
			break;
		}
	}
	out << std::fixed << std::setprecision(7) << total << "\n";
}

int main()
{
	int numOfTCs;
	in >> numOfTCs;
	std::vector<data> values(numOfTCs);
	for (int i = 0; i < numOfTCs; ++i)
	{
		in >> values[i].c >> values[i].f >> values[i].x;
	}
	for (int i = 1; i <= numOfTCs; ++i)
	{
		out << "Case #" << i << ": ";
		printMin(values[i-1]);
	}
}
