// ProblemA.cpp : Defines the entry point for the console application.
//
// BribeThePrisoners.cpp : Defines the entry point for the console application.
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

//const double PI = 3.14159265;

void work()
{
	long long r, t;
	scanf("%lld %lld", &r, &t);

	long long result = 0;

	long long needed;
	do
	{
		long long firstRad = r * r;
		long long secondRad = (r+1) * (r+1);

		needed = secondRad - firstRad;

		if (t >= needed)
		{
			result++;

			r+=2;
			t-= needed;
		}

	} while (t >= needed);

	printf("%lld\n", result);
}

int _tmain(int argc, _TCHAR* argv[])
{
	//freopen("SampleData.in", "r", stdin);
	freopen("A-small-attempt0 (1).in", "r", stdin);
	freopen("A-small-attempt0 (1).out", "w", stdout);

	int tt;
	scanf("%d", &tt);
	REP(it, tt)
	{
		printf("Case #%d: ", it + 1);

		work();
	}

	return 0;
}

