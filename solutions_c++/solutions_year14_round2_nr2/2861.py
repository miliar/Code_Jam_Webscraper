#include "CodeJam.h"
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <time.h>

using namespace std;


void TestCase(std::istream& is, std::ostream& os)
{
	int A, B, K;
	is >> A >> B >> K;
	vector<int> results;

	for( int a = 0; a < A; ++a )
	{
		for( int b = 0; b < B; ++b )
		{
			int result = a & b;
			if( result < K )
				results.push_back(result);
		}
	}

	os << results.size() << endl;
}
