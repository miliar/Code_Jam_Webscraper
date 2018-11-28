#include <fstream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <limits>
#include <boost/smart_ptr/scoped_array.hpp>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("output.txt");

double calc(double c, double f, double x)
{
	double res = std::numeric_limits<double>::max();
	double curTime = 0;
	double curSpeed = 2;
	int num = 0;
	while(curTime < res)
	{
		res = min(res,  curTime + x / curSpeed);
		curTime += c / curSpeed;
		curSpeed += f;
		++num;
	}
	return res;
}

int main()
{
	int T;
	fin >> T;
	fout << setprecision(7) << fixed;
	for(int i = 1; i <= T; ++i)
	{
		double c, f, x;
		fin >> c >> f >> x;
		fout << "Case #" << i << ": " << calc(c, f, x) << std::endl;
	}
}
