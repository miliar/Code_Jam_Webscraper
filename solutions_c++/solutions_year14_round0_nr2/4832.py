#include<iostream>
using namespace std;
#include<stdio.h>

#define eps 1e-6
bool isGreater(double a, double b)
{
	if(a > b)
		return true;
	return false;
}

int main()
{
	int test, testcase;
	int g1, g2;
	int i, j;
	freopen("D:\\codejam\\B-small-attempt2.in", "r", stdin);
	freopen("d:\\codejam\\out.txt", "w", stdout);
	double lowest = 50005.0;
	cin >> testcase;
	double C, F, X;
	double timeForBuy, timeForAchieve, nowRate, remaining;

	for(test = 1;test<=testcase;test++)
	{
		lowest = 50005.0;
		cin >> C >> F >> X;
		cout << "Case #" << test << ": ";
		int tryWith = 1;
		nowRate = 2;
		timeForAchieve = 0.0;
		timeForBuy = X/nowRate;
		double temp = timeForAchieve+timeForBuy;
		if(isGreater(lowest, temp))
			lowest = temp;

		for(i=1;;i++)
		{
			timeForAchieve = 0.0;
			nowRate=2.0;
			for(j=1;j<=i;j++)
			{
				timeForAchieve+= (C/nowRate);
				nowRate+=F;
			}
			timeForBuy = X/nowRate;
			double temp = timeForAchieve+timeForBuy;
			if(isGreater(lowest, temp))
				lowest = temp;
			else
			{
				printf("%.7lf\n", lowest);
				break;
			}
		}
	}
	return 0;
}