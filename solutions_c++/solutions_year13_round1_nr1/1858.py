// gj.cpp
//

#include <assert.h>

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <utility>

using namespace std;

typedef unsigned char uchar;
typedef unsigned int uint;
typedef unsigned __int64 uint64;

#define EPS (1E-10)
#define PI 3.1415926535897932384626433832795

int main(int argc, char* argv[])
{
	uint64 cases;
	cin >> cases;

	for (uint64 i = 1; i <= cases; ++i)
	{
		uint64 r, t;
		cin >> r >> t;

		uint64 c = 0,
			   sp = 0;
		while (sp <= t)
		{
			sp += 2 * r + 1;
			if (sp <= t)
				++c;

			r += 2;
		}

		cout << "Case #" << i << ": " << c << endl;
	}

	return 0;
}
