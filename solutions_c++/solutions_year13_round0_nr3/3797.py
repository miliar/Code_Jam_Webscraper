#ifdef DEBUG_OUTPUT
#include "debug_output.h"
#else
#define DEBUG(x)
#endif

#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <memory.h>
#include <set>
#include <map>
#include <cstdio>
#include <cassert>
#include <math.h>
using namespace std;


// Enlarge MSVS stack size
#pragma comment(linker, "/STACK:16777216")

#define pb push_back
#define all(c) c.begin(), c.end()
#define mp(x, y) make_pair(x, y)
#define sz(x) static_cast<int>(x.size())
typedef long long int64;

typedef vector<vector<int>> vvi;
typedef vector<int> vi;

template<class T> T sqr(const T& t) {return t * t;}
template<class T> T abs(const T& t) {return ((t > 0) ? (t) : (-t));}

void initialize()
{
    freopen("_.in", "r", stdin);
    freopen("_.out", "w", stdout);
	std::ios_base::sync_with_stdio (false);
}

bool IsFair(int k)
{
	stringstream ss;
    ss << k;
    string kStr = ss.str();

	int len = kStr.length();
	for (int i = 0; i < len / 2; i++)
	{
		if (kStr[i] != kStr[len - i - 1])
			return false;
	}
	return true;
}

bool Check(int k)
{
	bool isFair = IsFair(k);
	if (!isFair)
		return false;

	double sqrtDouble = sqrt((double)k);
	int sqrtInt = sqrtDouble;
	double dif = sqrtDouble - sqrtInt;

	if (dif != 0)
		return false;

	return
		IsFair(sqrtInt);
}

int CalcCountOfFairSquare(int min, int max)
{
	int count = 0;
	for (int k = min; k <= max; k++)
	{
		bool ok = Check(k);
		if (ok)
			count++;
	}
	return count;
}

int main()
{
    initialize();

	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++)
	{
		int min, max;
		cin >> min >> max;
		assert(min <= max);

		cout << "Case #" << i + 1 << ": " << CalcCountOfFairSquare(min, max) << endl;
	}

    
    return 0;
}
