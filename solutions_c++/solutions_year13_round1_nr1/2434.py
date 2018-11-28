// Test.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>

using namespace std;

string winner(char c)
{
	string res;
	res += c;
	res += " won";
	return res;
}


long long calc (long long r, long long t)
{
	long double a = 2.0;
	long double b = 2.0 * r - 1.0;
	long double c = (long double) -t;
	long double n = (-b + sqrt(b * b - 4.0 * a * c)) / 2.0 / a;
	long long nn = (long long) floor(n);
	long long ct = 2 * nn * nn + (2 * r - 1) * nn;
	if (ct > t)
		for (; ct > t && nn > 1; --nn)
			ct -= 2 * r * + 4 * nn - 3;
	else if (ct < t)
		for (; ct < t - (2 * r * + 4 * (nn + 1) - 3);)
			ct += 2 * r * + 4 * (++nn) - 3;
	return nn;
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int c = 0; c < numCases; ++c) 
	{
		long long r, t;
		cin >> r >> t;

		long long n = calc(r, t);
		
		cout << "Case #" << c+1 << ": " << n << endl;
	}

	return 0;
}

