#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

double val;

double doit(double c, double f, double x, double factories, double t)
{
	cout << c << " " << f << " " << x << " " << factories << endl;
	double power = 2 + factories * f;
	double res = x / power;
	if (res < (c / power))
		return res;
	if (res + t < val)
		val = res + t;
	if (c / power + t > val)
		return res;
	double res2 = c / power + doit(c, f, x, factories + 1, t + c / power);
	if (res < res2)
		return res;
	return res2;
}

int main()
{
	fstream file("B-small-attempt0.in");
	fstream output("output.txt");
	std::string s;
	std::getline(file, s);
	int n = atoi(s.c_str());
	for (int i = 0; i < n; ++i)
	{
		double c, f, x;
		file >> c >> f >> x;
		cout << i << " " << c << " " << f << " " << x << endl;
		val = x / 2;
		output << "Case #" << i+1 << ": " << setprecision(20) << doit(c, f, x, 0, 0) << endl;
	}
	file.close();
	output.close();
}