// ProblemB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <iostream>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <functional>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define clr(x) memset((x), 0, sizeof(x))


double doSolve(double C, double F, double X){
	if (X <= 0.0)
	{
		return 0.0f;
	}

	double currentCPS = 2.0;
	
	if (X <= C)
	{
		return X/currentCPS;
	}

	double current = C;
	double timeSpent = C/currentCPS;
	do{
		if (current >= C)
		{
			//we have 2 choices
			double timeToXByJustWaiting = (X - current) /  currentCPS;
			double timeToXByBuyingFarm =  (X + C - current) /  (currentCPS+F);

			if (timeToXByJustWaiting < timeToXByBuyingFarm)
			{
				current = X;
				timeSpent += timeToXByJustWaiting;
			}
			else
			{
				current -= C;
				currentCPS += F;
			}
		}
		else
		{
			//we need to wait until we have enough (or we are done)
			double timeToC = (C - current) / currentCPS;
			double timeToX = (X - current) / currentCPS;

			if (timeToX < timeToC)
			{
				current = X;
				timeSpent += timeToX;
			}
			else
			{
				current = C;
				timeSpent += timeToC;
			}

		}
	} while (current < X);

	return timeSpent;
}


int _tmain(int argc, _TCHAR* argv[])
{
	freopen("demo.in", "r", stdin);

	int tt;
	scanf("%d", &tt);
	REP(it, tt)
	{
		printf("Case #%d: ", it + 1);

		double C, F, X;
		scanf("%lf", &C);
		scanf("%lf", &F);
		scanf("%lf", &X);
	
		//get the number of goes
		double result = doSolve(C,F,X);

		printf("%lf\n", result);
	}

	return 0;
}

