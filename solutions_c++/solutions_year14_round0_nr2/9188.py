// Cookie_Clicker_Alpha.cpp : Defines the entry point for the console application.
//

#pragma warning(disable : 4996)

#include "stdafx.h"
#include <fstream> // You should include this library
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int T, counter = 1;
	double C, F, X, minTime = 0, number_cookies_per_second = 2;

	freopen("D:\\My works\\GoogleJam\\Problem B\\submissions\\input.in","r",stdin); // For reading input
	cin >> T;

	cout << T << endl;

	ofstream out("D:\\My works\\GoogleJam\\Problem B\\submissions\\output.out");

	do
	{
		cin >> C >> F >> X;

		cout << C << " " << F << " " << X << " ";

		while (true)
		{
			if ( (X/number_cookies_per_second) > ((C/number_cookies_per_second) + (X/(number_cookies_per_second + F))) )
			{
				minTime += (C/number_cookies_per_second);
				number_cookies_per_second += F;
			}
			else
			{
				minTime += (X/number_cookies_per_second);
				break;
			}
		}

		cout << endl <<"Case #" << counter << ": " << setprecision(9) << minTime << endl;

		out << "Case #" << counter << ": " << setprecision(9) << minTime << endl;

		counter++;
		minTime = 0;
		number_cookies_per_second = 2;
		T--;

		cout << endl;

	} while (T > 0);

	out.close();

	return 0;
}

