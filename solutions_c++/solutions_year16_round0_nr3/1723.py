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
const i64 base = 10000000000000000;

i64 n, m, c, d[15];
bitset <40> bs;
string s;
i64 t[2];


bool check(i64 di)
{
	i64 rem = t[1] % di;

	for (int i = 0; i < 16; ++i)
		rem = (rem * (10 % di)) % di;
	rem = (rem + (t[0] % di)) % di;

	return !rem;
}

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

	cin >> n >> n >> m;
	printf("Case #1:\n");

	for (i64 i = (i64)1 << (n - 1); c < m; ++i)
	{
		if (!(i % 2)) continue;
		bs = i;
		s = bs.to_string();
		for (int j = 2; j < 11; ++j)
			d[j] = 0;
		
		for (i64 j = 2; j < 11; ++j)
		{
			t[0] = t[1] = 0;
			for (i64 k = 0; k < s.size(); ++k)
			{
				t[0] = t[0] * j + s[k] - '0';
				t[1] *= j;
				if (t[0] > base)
				{
					t[1] += t[0] / base;
					t[0] %= base;
				}
			}

			for (i64 k = 2; k*k < 1000000000; ++k)
				if (check(k))
				{
					d[j] = k;
					goto a;
				}

			goto b;

		a: {}
		}
		
		++c;
		s = s.substr(size_t(40 - n), 40);

		cout << s << ' ';
		for (i64 j = 2; j < 11; ++j)
			printf("%d ", d[j]);

		printf("\n");


	b: {}
	}


	return 0;
}
