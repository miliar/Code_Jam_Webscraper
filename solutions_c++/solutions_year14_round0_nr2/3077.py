// Syed Ghulam Akbar
// CodeJam 2014

#include <cstdio>
#include <iostream>
#include <iomanip>      // std::setprecision
#include <string>

using namespace std;

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	for (int test=1;test<=testCount;test++) {
		double C, F, X, rate, time = 0, t1, t2;
		long total = 0;

		cin >> C >> F >> X;

		// Start with rate of 2
		rate = 2;

		// Keep generating the cookies until our target is achieved
		while (total < X)
		{
			// Cost if we directly generate cookies
			t1 = X / rate;

			// Cost if we instead buy a form
			t2 = (C / rate) + (X / (rate + F));

			// Better to purchase cookie farm
			if (t2 < t1)
			{
				time += (C / rate);
				rate += F;
			}
			else
			{
				// As we can build all cookies with current rate faster, we are done
				time += t1;
				break;
			}
		}

		std::cout << "Case #" << test << ": ";
		std::cout << std::fixed << std::setprecision(7) << time << endl;
	}
}
