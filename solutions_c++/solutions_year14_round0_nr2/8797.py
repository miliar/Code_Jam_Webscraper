#include <iostream>
#include <vector>

using namespace std;

double bestTime(double C, double F, double X)
{
	double f = 2.0;
	double minTime = X / f;
	double timeElapsed = 0;
	while (true)
	{
		timeElapsed += (C/f);
		f += F;
		double newTime = timeElapsed + X / f;
		if (newTime >= minTime)
			break;
		minTime = newTime;
	}
	
	return minTime;
}

int main()
{
	int T;
	cin >> T;
	double C,F,X;
	for (int t = 1; t <= T; ++t)
	{
		cin >> C >> F >> X;
		double minTime = bestTime(C,F,X);
		printf("Case #%d: %.7f\n", t, minTime);
	}
	return 0;
}