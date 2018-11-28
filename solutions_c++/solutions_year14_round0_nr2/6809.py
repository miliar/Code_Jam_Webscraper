// CookieClickerAlpha.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

long double epsilon = 0.0000000000001;

long double cookies = 0.0;
long double cookiesPerSecond = 2.0;
long double t = 0.0;
long double C, F, X;

void GainCookies(long double amount)
{
	if (amount <= 0)
		return;
	t += amount / cookiesPerSecond;
	cookies += amount;
}

long double Solve()
{
	cookies = 0.0;
	cookiesPerSecond = 2.0;
	t = 0.0;	
	while (cookies < X - epsilon)
	{
		if (cookies < C)
		{
			GainCookies(min(C-cookies, X-cookies));
		}
		else
		{
			long double timeWithoutFarm = (X - cookies) / cookiesPerSecond;
			long double timeWithFarm = (X - (cookies - C)) / (cookiesPerSecond + F);
			if (timeWithFarm < timeWithoutFarm - epsilon)
			{
				cookies -= C;
				cookiesPerSecond += F;
			}
			else
			{
				GainCookies(X-cookies);
			}
		}
	}
	return t;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inputFile("B-large.in");
	if (!inputFile.is_open())
	{
		cerr << "Error reading file" << endl;
		return 1;
	}

	int T;
	inputFile >> T;

	ofstream outputFile("output.txt");
	ostream &output = outputFile;
	output  << fixed << setprecision(6);
	for (int i = 0; i < T; ++i)
	{
		//long double C, F, X;
		inputFile >> C >> F >> X;	
		output << "Case #" << (i+1) << ": " << Solve() << endl;
	}

	return 0;
}

