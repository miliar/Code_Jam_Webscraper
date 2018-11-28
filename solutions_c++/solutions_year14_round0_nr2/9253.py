/*
 * qualA.cpp
 *
 *  Created on: 2014-04-12
 *      Author: aabdelsa
 */

#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <iomanip>

using namespace std;

int main ()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);

	int cases;
	cin >> cases;

	for ( int t = 1; t<=cases; t++)
	{
		double C,F,X;
		cin >> C >> F >> X;

		double mnTime = X/2.0;
		double curRate = 2.0;
		double passedTime = 0;
		while (true)
		{
			//cout << mnTime << endl;
			double waitTime = C/curRate;
			double newRate = curRate + F;
			double totalTime = passedTime + waitTime + (X/newRate);
			if ( totalTime > mnTime)
				break;
			passedTime += waitTime;
			mnTime = totalTime;
			curRate = newRate;
		}
		cout << fixed;
		cout << "Case #" <<t<<": " << setprecision(7)<< mnTime << endl;
	}
	return 0;
}
