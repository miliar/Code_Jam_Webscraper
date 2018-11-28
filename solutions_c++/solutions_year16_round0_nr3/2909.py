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

uint64 cnt(uint64 b, uint64 n)
{
	if (b == 2)
		return n;

	uint64 r = 0,
		   cb = 1;
	while (n)
	{
		r += (n & 1) * cb;
		cb *= b;
		n >>= 1;
	}

	return r;
}

uint64 isp(uint64 x)
{
	for (uint64 i = 3; i * i <= x; i += 2)
	{
		if (x % i == 0)
			return i;
	}
	return 0;
}

uint cbs(uint64 v)
{
	uint r = 0;
	while (v)
	{
		r += v & 1;
		v >>= 1;
	}
	return r;
}

struct qq
{
	uint64 a[5];
};

int main(int argc, char* argv[])
{
    uint64 cases;
    cin >> cases;

    for (uint64 cs = 1; cs <= cases; ++cs)
    {
		uint64 n, j;
		cin >> n >> j;

		uint64 st = (1 << n) + 1,
			   fn = st * 2;

		uint r = 0;
		vector<qq> v;

		for (uint64 i = st; i < fn && v.size() < j; i += 2)
		{
			if (cbs(i) == 6 && isp(i) == 3)
			{
				qq qs;
				qs.a[0] = i;

				uint qn = 1;
				for (uint q = 4; q <= 10; q += 2)
				{
					uint64 cn = cnt(q, i),
							d = 0;

					uint64 p = isp(cn);
					if (p)
						qs.a[qn++] = p;
					else
						break;
				}

				if (qn == 5)
					v.push_back(qs);
			}
		}

		cout << "Case #" << cs << ":\n";
		for (uint i = 0; i < j; ++i)
		{
			cout << cnt(10, v[i].a[0]) << ' ' << 3;
			for (uint k = 1; k < 5; ++k)
				cout << ' ' << 2 << ' ' << v[i].a[k];
			cout << '\n';
		}

    }

    return 0;
}
