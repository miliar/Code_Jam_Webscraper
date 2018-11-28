#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <utility>
#include <algorithm>
#include <utility>
#include <functional>
#include <cmath>
#include <string>
#include <queue>
#include <numeric>
#include <map>
#include <set>

using namespace std;


int main(int argc, char *argv)
{
	ifstream ifs("B-large.in");
	ofstream ofs("B-large.out");
	unsigned int nb_cases;
	ifs >> nb_cases;
	for (unsigned int i = 0; i < nb_cases; i++)
	{
		ofs << "Case #"<<i+1<<": ";
		// do for each case
		double C, F, X;
		ifs >> C;
		ifs >> F;
		ifs >> X;
		double tm = 0.0;
		double v = 2.0;
		double t1 = C/v + X/(v+F);
		double t2 = X/v;
		while (t1 < t2)
		{
			tm += C/v;
			v += F;
			t1 = C/v + X/(v+F);
			t2 = X/v;
		}
		tm += t2;
		//ofs.width(12);
		ofs.setf(std::ios::fixed, std:: ios::floatfield);
		ofs.precision(7);
		ofs << tm;
		ofs << endl;
	}
	return 0;
}