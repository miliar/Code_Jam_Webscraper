#include <fstream>
#include <string>
#include <list>
#include <sstream>
#include <iomanip>
using namespace std;


double getResult(double c, double f, double x)
{
	double power = 2.0;
	double time = 0.0;
	double resultOld = time + x / power;
	double resultNew;
	for (int i = 1; true; ++i)
	{
		time += c / power;
		power = 2.0 + f * i;
		resultNew = time + x / power;
		if(resultNew > resultOld)
		{
			return resultOld;
		}
		resultOld = resultNew;
	}
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	out << std::fixed;
	out << std::setprecision(7);
	int t;
	in >> t;
	for(int i = 0; i < t; ++i)
	{
		double c, f, x;
		in >> c >> f >> x;
		out << "Case #" << i+1 << ": " << getResult(c, f, x) << "\n";
	}
	return 0;
}
