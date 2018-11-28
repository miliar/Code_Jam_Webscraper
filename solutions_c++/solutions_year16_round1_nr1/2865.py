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

int main(int argc, char* argv[])
{
	uint64 cases;
    cin >> cases;

    for (uint64 cs = 1; cs <= cases; ++cs)
    {
		string s;
		cin >> s;

		string p;
		p += s[0];
		for (uint i = 1; i < s.size(); ++i)
		{
			if (s[i] > p[0])
				p = s[i] + p;
			else if (s[i] < p[0])
				p += s[i];
			else
			{
				bool o = true;
				for (uint j = 1; o && j < p.size(); ++j)
				{
					if (p[j] > s[i])
					{
						p += s[i];
						o = false;
					}
					else if (p[j] < s[i])
					{
						p = s[i] + p;
						o = false;
					}
				}

				if (o)
					p += s[i];
			}
		}

		cout << "Case #" << cs << ": " << p << '\n';
    }

    return 0;
}
