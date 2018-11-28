// 2013_1A.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <math.h>
#include <Windows.h>
using namespace std;

 
double k1(double n)
{
	return (static_cast<double>(4) * n * n * n - n ) / static_cast<double>(3);
}

double k2(double n)
{
	return n * (n+1) * (static_cast<double>(2)*n+1) * static_cast<double>(2) / static_cast<double>(3);
}

double c1(double n)
{
	return (static_cast<double>(2) * n * n + n);
}

double c2(double n)
{
	auto v = ( n * n * static_cast<double>(2) +  n * static_cast<double>(3));
	return v;
}


void A(int N)
{
	unsigned __int64 dr, dt;

	cin >> dr;
	cin >> dt;

	double r = static_cast<unsigned __int64>(dr);
	double t = static_cast<unsigned __int64>(dt);

	unsigned __int64 ans;
	if (dr%2)
	{
		if (dr>2)
		{
			t+= c1((r-1)/2);
		}
		ans = sqrtl(1+8*t);
		ans--;
		ans/=4;
		
		if (dr>2)
		{
			ans -= (r-1)/2;
		}
	}
	else
	{
		if (dr>3)
		{
			t+= c2((r-2)/2);
		}
		ans = sqrtl(t*8+9);
		ans-=3;
		ans/=4;
		
		if (dr>3)
		{
			ans -= (r-2)/2;
		}
	}

	printf("Case #%d: %I64d\n", N+1, ans);
};

int _tmain(int argc, _TCHAR* argv[])
{
	int N;

	cin >> N;

	for(int i=0;i<N;i++)
	{
		A(i);	
	}
	getchar();
	return 0;
	
}

