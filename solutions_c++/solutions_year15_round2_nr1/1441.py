#include "stdafx.h"

#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <array>

using namespace std;

std::array<int, 1000005> steps;

void precalc()
{
	std::fill(steps.begin(), steps.end(), 2000000);

	steps[1] = 1;

	for( int i = 1; i < 1000001 ; ++i)
	{
		int st = steps[i];

		if ( steps[i+1] > st )
		{
			steps[i+1] = st + 1;
		}
		int num = i;
		int rev = 0;
		while (num > 0)
		{
			rev *=10;
			rev+= num %10;
			num/=10;
		}
		if (steps[rev] > st+1)
		{
			steps[rev] = st+1;
		}
	}
	/*for( int i = 1; i < 1000001 ; ++i)
	{
		cout << i << " " << steps[i] << endl;
	}*/
}

int testcase()
{
	int N;
	cin >> N;
	return steps[N];
} 

int main()
{
	precalc();
	int n;
	std::cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		int r = testcase();
		std::cout << "Case #" << i+1 << ": " << r << std::endl;
	}
	
	return 0;
}