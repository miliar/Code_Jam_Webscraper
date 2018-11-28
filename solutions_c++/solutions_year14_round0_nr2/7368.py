#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

double minTime(double v, double c, double f, double x)
{
	double m = x / v;
	double tempTime = 0.0;
	int buys = 0;
	double tempResult = x / (v + buys*f) + tempTime;
	for (int k = 0; k < (int)x*10; ++k)
	{
	    if (tempResult < m)
            m = tempResult;
		tempTime += c / (v + buys*f);
		buys++;
		tempResult = x / (v + buys*f) + tempTime;
	}
	return m;
}

int main(int argc, char const *argv[])
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
	int times;
	double v = 2;
	double c, f, x;
	fin >> times;
	for (int t = 0; t < times; ++t)
	{
		fin >> c >> f >> x;
		fout << "Case #" << (t+1) << ": " << fixed << setprecision(7) << minTime(v, c, f, x) << endl;
	}
	return 0;
	fin.close();
	fout.close();
}
