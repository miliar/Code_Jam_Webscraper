#include <iostream>
#include <iomanip>

using namespace std;

double deal(double rate, double c, double f, double x)
{
	double time1 = x/rate;
	double time2 = c/rate + x/(rate+f);

	if (time1 <= time2)
	{
		return time1;
	}
	else
	{
		return c/rate + deal(rate+f, c, f, x);
	}
}

int main(void)
{
	int cases;

	double c;
	double f;
	double x;

	double rate = 2.0;
	double time = 0.0;

	cin >> cases;

	for (int i = 0; i < cases; i++)
	{
		cin >> c >> f >> x;
		time = deal(rate, c, f, x);
		cout << "Case #"<< i+1 << ": " << fixed << setprecision(7) << time <<endl;
	}
	return 0;
}
