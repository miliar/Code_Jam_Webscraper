// gj.cpp
//

#include <assert.h>

#include <fstream>
#include <sstream>
#include <stack>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

typedef unsigned char uchar;
typedef unsigned int uint;
typedef unsigned __int64 uint64;

#define EPS (1E-10)
#define PI 3.1415926535897932384626433832795

uint v[10];

void cnt(uint64 n)
{
	while (n)
	{
		v[n % 10] = 1;
		n /= 10;
	}
}

int main(int argc, char* argv[])
{
    uint64 cases;
    cin >> cases;

    for (uint64 cs = 1; cs <= cases; ++cs)
    {
		uint64 n;
		cin >> n;

		if (n == 0)
			cout << "Case #" << cs << ": " << "INSOMNIA" << "\n";
		else
		{
			fill(v, v + 10, 0);
			uint64 s = 1;
			do
			{
				cnt(n * s);
				++s;
			} while (accumulate(v, v + 10, 0) < 10);

			cout << "Case #" << cs << ": " << n * (s - 1) << "\n";
		}
    }

    return 0;
}
