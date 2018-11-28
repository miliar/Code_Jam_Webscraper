/*
 * problemA.cpp
 *
 *  Created on: Apr 11, 2014
 *      Author: filipebraida
 */
#include<iostream>
#include <iomanip>
#include<stdio.h>

using namespace std;

int main(void)
{
	int test_cases;
	double c, f, x;

	cin >> test_cases;

	for(int n = 0; n < test_cases; n++)
	{
		cin >> c;
		cin >> f;
		cin >> x;

		double cookies = 0;
		double rate = 2;
		double time = 0;
		double parcialTotal = 0;
		double timeAnterior = (x - cookies) / rate;

		do
		{
				// nao chegou no limite
				time = time + (c / rate);

				rate = rate + f;

				parcialTotal = time + (x - cookies) / rate;

				if(timeAnterior < parcialTotal)
					break;
				else
					timeAnterior = parcialTotal;
		} while(true);

		cout << "Case #" << n + 1 << ": ";

		printf("%.7f\n", timeAnterior);
		cin.get();
	}

	return 0;
}
