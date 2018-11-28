// gj.cpp
//

#include <assert.h>

#include <fstream>
#include <iomanip>
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

char s[100][101];
uint si[100],
	 cc[100];

int main(int argc, char* argv[])
{
	uint64 cases;
	cin >> cases;

	for (uint64 cs = 1; cs <= cases; ++cs)
	{
		uint n;
		cin >> n;

		for (uint i = 0; i < n; ++i)
			cin >> s[i];

		bool ok = true;
		char c = s[0][0];
		uint r = 0;
		fill(si, si + n, 0);

		while (ok)
		{
			for (uint i = 0; i < n; ++i)
			{
				if (s[i][si[i]] != c)
				{
					ok = false;
					break;
				}
			}

			if (!ok || c == 0)
				break;

			fill(cc, cc + n, 0);
			uint ac = 0;
			for (uint i = 0; i < n; ++i)
			{
				while (s[i][si[i]] == c)
					++si[i], ++cc[i], ++ac;
			}

			c = s[0][si[0]];

			uint m = (ac + n / 2) / n;
			for (uint i = 0; i < n; ++i)
				r += m > cc[i] ? m - cc[i] : cc[i] - m;
		}

		if (ok)
			cout << "Case #" << cs << ": " << r << "\n";
		else
			cout << "Case #" << cs << ": Fegla Won\n";
	}

	return 0;
}
