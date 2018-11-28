#include <iostream>
#include <cmath>
#include <stdio.h>
using namespace std;
double c, f, x;

double calc(double req, double rate, double time)
{
	double nhee = req/rate;
	double bhandi = (c/rate)+(req/(rate+f));
	if(bhandi < nhee)
		return calc(req, rate+f, time+(c/rate));
	return time+nhee;
}

int main()
{
	int ite;
	cin>>ite;
	for(int it=1;it<=ite;it++)
	{
		cin>>c>>f>>x;
		printf("Case #%d: %.7lf\n",it, calc(x, 2.0, 0.0));
	}
	return 0;
}