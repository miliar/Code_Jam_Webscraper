#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm>
#include <iostream> 
#include <string.h> 
#include <stdlib.h>
#include <complex>
#include <sstream> 
#include <fstream>
#include <numeric>
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

#define N 1009

char str[N];

int main()
{
	int tests, k, i;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; test++)
	{
		scanf("%s %d", str, &k);
		int n = strlen(str);
		int res = 0;
		for(i = 0; i + k - 1 < n; i++)
		{
			if (str[i] == '-')
			{
				for (int j = 0; j < k; j++)
					str[i + j] ^= '-' ^ '+';
				res++;
			}
		}
		if (count(str, str + n, '-'))
			printf("Case #%d: IMPOSSIBLE\n", test);
		else
			printf("Case #%d: %d\n", test, res);
	}
}