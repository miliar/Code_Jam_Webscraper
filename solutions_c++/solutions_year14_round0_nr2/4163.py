#include <cstdio>
#include <iostream>
using namespace std;

double c, inc;

double min(double a, double b)
{
	return a > b ? b : a;
}

double f(double rate, double x)
{
	if ((c/rate + x/(rate+inc)) > x/rate ) return x / rate;
	double a = f(rate + inc, x) + c / rate;
	double b = x / rate;
	return min(a, b);
}

double iterativeF(double rate, double x)
{
	double acum = 0.00;
	while ((c / rate + x / (rate + inc)) < x / rate)
	{
		acum += c / rate;
		rate += inc;
	}
	return acum + x / rate;
}

int main()
{
	int t;
	int caso = 1;
	cin >> t;
	while (t--)
	{
		double x;
		cin >> c >> inc >> x;
		printf("Case #%d: ",caso++);
		printf("%.7lf\n", iterativeF(2, x));
	}
	return 0;
}