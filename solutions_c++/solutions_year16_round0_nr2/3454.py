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

		uint64 r = 0;
		uint sz = s.size();

		for (uint i = 0; i < sz; )
		{
			uint p = 0;
			while (i < sz && s[i] == '+')
				++i, p = 1;

			uint m = 0;
			while (i < sz && s[i] == '-')
				++i, m = 1;

			if (m)
				r += p + m;
		}

		cout << "Case #" << cs << ": " << r << '\n';
    }

    return 0;
}
