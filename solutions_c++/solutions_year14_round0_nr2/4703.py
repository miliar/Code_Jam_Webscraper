#include <iostream>
#include <cstdio>

using namespace std;

long double getMyTime(long double myRate, long double c, long double f, long double x)
{
	long double tim = 0, myAnswer = 0;
	tim = c / myRate;
	if(tim + x / (myRate + f) < x / myRate)
	{
		myAnswer = tim + getMyTime(myRate + f, c, f, x);
	}
	else
		myAnswer = x / myRate;

	return myAnswer;
}

int main()
{
	int T;
	cin >> T;

	long double c, f, x, calcTime;

	for(int i = 0; i < T; ++i)
	{
		cin >> c;
		cin >> f;
		cin >> x;

		if(x < c || f == 0)
		{
			calcTime = x / 2;
		}
		else
		{
			calcTime = getMyTime(2.0, c, f, x);
		}

		printf("Case #%d: %0.7Lf\n", i+1, calcTime);
	}

}