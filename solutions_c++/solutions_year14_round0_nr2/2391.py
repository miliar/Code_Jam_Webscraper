#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <iomanip>
#include <utility>
#include <sstream>
#include <unordered_map>
#include <unordered_set>

using namespace std;


int main()
{
	unsigned t;
	scanf_s( "%u", &t );
	
	for( unsigned i = 1; i <= t; ++i )
	{
		using ld = long double;
		const ld initialRate = 2.0;

		ld farmCost;
		cin >> farmCost;
		ld farmRate;
		cin >> farmRate;
		ld goal;
		cin >> goal;

		ld currentRate = initialRate;

		ld solution = goal / initialRate;

		for( ld t = 0.0; ; )
		{	
			t += farmCost / currentRate;
			currentRate += farmRate;
			ld newSolution =  t + goal / currentRate;
			if( newSolution > solution )
			{
				break;
			}
			solution = newSolution;
		}

		printf( "Case #%u: %.7f\n", i, solution );
	}

	return 0;
}
