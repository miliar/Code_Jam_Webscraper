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

uint p[1000],
	 sm,
	 n;

bool chk(uint x)
{
	--sm;
	--p[x];

	for (uint i = 0; i < n; ++i)
	{
		if (p[i] > sm - p[i])
		{
			++sm;
			++p[x];
			return false;
		}
	}

	return true;
}

int main(int argc, char* argv[])
{
	uint64 cases;
	cin >> cases;

	for (uint64 cs = 1; cs <= cases; ++cs)
	{
		cin >> n;

		sm = 0;
		for (uint i = 0; i < n; ++i)
		{
			cin >> p[i];
			sm += p[i];
		}

		vector<string> v;
		while (true)
		{
			bool q = false;
			for (uint i = 0; i < n; ++i)
			{
				if (chk(i))
				{
					string s;
					s += i + 'A';
					v.push_back(s);
					q = true;
				}
			}

			if (!q)
				break;
		}

		uint st = 0;
		while (p[st] == 0)
		{
			++st;
			st %= n;
		}

		while (sm)
		{
			string s;
			s += st + 'A';
			--p[st];
			--sm;

			++st;
			st %= n;
			while (sm && p[st] == 0)
			{
				++st;
				st %= n;
			}
			s += st + 'A';
			--p[st];
			--sm;

			++st;
			st %= n;
			while (sm && p[st] == 0)
			{
				++st;
				st %= n;
			}

			v.push_back(s);
		}

		cout << "Case #" << cs << ":";
		for (uint i = 0; i < v.size(); ++i)
			cout << ' ' << v[i];
		cout << '\n';
	}

	return 0;
}
