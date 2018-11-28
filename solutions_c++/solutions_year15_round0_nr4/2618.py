// GCJ2015_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for (int qq=1;qq<=tt;qq++) {
		printf("Case #%d: ", qq);
		int X, R, C;
		scanf("%d", &X);
		scanf("%d", &R);
		scanf("%d", &C);

		if(X==1 && R>=1 && C>=1)
		{
			printf("GABRIEL\n");
			continue;
		}

		if(X==2 && ((R*C)%2==0))
		{
			printf("GABRIEL\n");
			continue;
		}

		if(X > (R*C))
		{
			printf("RICHARD\n");
			continue;
		}

		if((R*C)%X != 0)
		{
			printf("RICHARD\n");
			continue;
		}

		if(X>R && X>C)
		{
			printf("RICHARD\n");
			continue;
		}

		if(X>=(R+C))
		{
			printf("RICHARD\n");
			continue;
		}

		if((R==2||C==2) && X>=4)
		{
			printf("RICHARD\n");
			continue;
		}

		if((R>2||C>2) & X>=6)
		{
			printf("RICHARD\n");
			continue;
		}

		if(X > (2*C) || X > (2*R))
		{
			printf("RICHARD\n");
			continue;
		}
		printf("GABRIEL\n");
		if(X>2)
		{
			int test = 0;
		}


	}
	return 0;
}

