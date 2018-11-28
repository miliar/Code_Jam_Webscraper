#include <iostream>
#include <cstdio>

using namespace std;

double solve(double C, double F, double X)
{
	double secs = 0;
	double cc = 0;
	double rate = 2.0f;

	if(X < C)
	{
		secs = X/rate;
		return secs;
	}

	while(true)
	{
		double ttnf = (C-cc)/rate;

		double bt = X/(rate+F);
		double nbt = (X-C)/(rate);
		
		if(bt < nbt)
		{
			rate = rate + F;
			secs = secs + ttnf;
			cc = 0;
		}
		else
		{
			secs = secs + ttnf + nbt;
			break;
		}
	}
	
	return secs;
}

int main(int args, char** argv)
{
	int T = 0;
	cin >> T >> ws;

	for(int i = 1; i <= T; i++)
	{
		double secs = 0, C = 0, F = 0, X = 0;
		cin >> C >> F >> X >> ws;
		secs = solve(C, F, X);
		printf("Case #%d: %.7f\n", i, secs);
	}
	return 0;
}
