#pragma comment(linker, "/STACK:268435456")
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <fstream>
#include <functional>
#include <stdio.h>
#include <sstream>
#include <bitset>
#include <limits.h>
#include <stack>
using namespace std;

#define sqr(a) ((a)*(a))
typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;

const ld EPS = 1e-16;

i64 n;
string t;

int main()
{
	cout.precision(50);
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	cin >> n;

	for (int i = 0; i < n; ++i)
	{
		cin >> t;

		char tt = t[0];
		int c = 0;

		for (int i = 0; i < t.size(); ++i)
			if (tt != t[i])
			{
				++c;
				tt = t[i];
			}

		if (t.back() == '-')
			++c;

		printf("Case #%d: %I64d\n", i + 1, c);
	}


	return 0;
}
