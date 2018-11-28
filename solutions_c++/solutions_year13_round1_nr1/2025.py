#define _USE_MATH_DEFINES

#include <stdio.h>
#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
#include <math.h>
using namespace std;

typedef unsigned int uint;

int main(unsigned long argc, char* argv)
{
	uint T;
	cin >> T;
	for(uint i = 1; i <= T; ++i)
	{
		uint r;
		long long t;
		cin >> r >> t;
		uint circs = 0;

		while (t > 0)
		{
			++r;
			t -= 2*r - 1;
			if (t >= 0) ++circs;
			++r;
		}
		printf("Case #%d: %d\n", i, circs);
	}

	return 0;
}