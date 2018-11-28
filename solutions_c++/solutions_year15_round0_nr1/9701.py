// StandingOvation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"
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


int main()
{
	freopen("A-small-attempt4.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int q=1;q<=T;q++)
	{
		printf("Case #%d: ", q);
		int S;
		scanf("%d", &S);
		int A;
		scanf("%d", &A);
		int max = 0;
		int sum = 0;
		int last = 0;
		for (int x=0;x<=S;x++)
		{
			if (sum < x) 
				if (max < x-sum)
					max = x - sum;
			last = (int)(A/(pow(double(10),S+1-x)))*10;
			sum = sum + (int)A/(pow(double(10),S-x)) - last;
		}
		printf("%d\n",max);
	}
	return 0;
}

