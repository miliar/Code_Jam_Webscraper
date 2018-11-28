#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

void solver(int numCase)
{
	double C, F, X;
	double seconds = 0, rate = 2.0, waitAll, waitCookie;

	scanf("%lf %lf %lf", &C, &F, &X);
	while (true)
	{
		// wait until finish
		waitAll = X / rate;
		// wait until can buy new cookie + wait until finish with new rate
		waitCookie = C / rate + X / (rate + F);

		// if waiting is better
		if (waitAll <= waitCookie)
		{
			seconds += waitAll;
			break;
		}
		else
		{
			// better buy cookie
			seconds += 1.0 * C / rate;
			rate += F;
		}
	}

	printf("Case #%i: %.7lf\n", numCase, seconds);
}

int main()
{
	int numCase, cases;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%i", &cases);
	for (numCase = 1; numCase <= cases; numCase++)
		solver(numCase);

	return 0;
}