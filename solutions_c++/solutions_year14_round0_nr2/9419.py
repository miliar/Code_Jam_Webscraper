#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

// 2014Spring ProblemB
double solve(double C, double F, double X, double f0, double passedTime)
{
	double time = X / f0;
	double timeAddFactory = (C / f0) + (X / (f0 + F));
	if (time <= timeAddFactory)
		return passedTime + time;
	else
		return solve(C, F, X, f0 + F, passedTime + (C / f0));
}
int main()
{
	int testNum; cin >> testNum;
	for (int i = 1; i <= testNum; ++i)
	{
		double C, F, X; cin >> C >> F >> X;
		cout.precision(10);
		cout << "Case #" << i << ": " << solve(C, F, X, 2., 0.) << "\n";
	}
	return 0;
}
