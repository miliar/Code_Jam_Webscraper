#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm> 
#include <iostream> 
#include <string.h> 
#include <stdlib.h> 
#include <sstream> 
#include <fstream>
#include <ctype.h> 
#include <stdio.h> 
#include <bitset>
#include <vector> 
#include <string> 
#include <math.h> 
#include <time.h> 
#include <queue> 
#include <stack> 
#include <list>
#include <map> 
#include <set> 
#define Int long long 
#define INF 0x3F3F3F3F 
#define eps 1e-9
using namespace std;

int main()
{
	int tests, n, x, i, j, a;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		scanf("%d %d", &n, &x);
		multiset<int> S;
		for (i = 0; i < n; i++)
		{
			scanf("%d", &a);
			S.insert(a);
		}
		int res = 0;
		while (S.size())
		{
			auto a = *--S.end();
			S.erase(--S.end());
			res++;
			if (S.size())
			{
				auto u = S.upper_bound(x - a);
				if (u == S.begin())
					continue;
				u--;
				S.erase(u);
			}
		}
		printf("Case #%d: %d\n", test, res);
	}
}