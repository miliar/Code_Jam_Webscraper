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

i64 n, t;

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

	scanf("%d\n", &n);

	for (int i = 0; i < n; ++i)
	{
		scanf("%d\n", &t);

		if (0 == t)
		{
			printf("Case #%d: INSOMNIA\n", i + 1);
			continue;
		}

		int c = 1023, j = 0;

		while (c)
		{
			++j;
			
			i64 tt = t * j;

			while (tt > 0)
			{
				c = c & ~(1 << (tt % 10));
				tt /= 10;
			}
		}

		printf("Case #%d: %I64d\n", i + 1, t * j);
	}


	return 0;
}
