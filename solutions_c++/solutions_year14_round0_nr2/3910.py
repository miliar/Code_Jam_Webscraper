#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
using namespace std;

int main()
{
	ifstream fin("B.in");
	ofstream fout("B.out");
	int t;
	double rate, c, f, x;
	fin >> t;
	for (int urns = 0; urns < t; ++urns)
	{
		fout << "Case #" << urns+1 << ": ";
		double best = 9999999999, tim = 0;
		rate = 2;
		fin >> c >> f >> x;
		while(1)
		{
			if (tim + x/rate < best) best = tim + x/rate;
			else break;
			tim += c/rate;
			rate += f;
		}
		fout << fixed << setprecision(7) << best << endl;
	}
}
