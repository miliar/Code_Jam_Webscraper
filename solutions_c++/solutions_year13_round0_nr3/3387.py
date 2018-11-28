#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
using namespace std;

unsigned long long inStart, inEnd, rootStart, rootEnd;

void Calculate(int test);
bool isP(unsigned long long a);

int main(void)
{
	freopen("A-small.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int nTest;

	scanf("%d", &nTest);
	for (int i = 0; i < nTest ; i++)
	{
		scanf("%llu %llu", &inStart, &inEnd);
		rootStart = (unsigned long long)sqrt((long double)inStart) -1;
		rootEnd= (unsigned long long)sqrt((long double)inEnd) + 1;
		Calculate(i+1);
	}
	return 1;
}

void Calculate(int test)
{
	int res = 0;
	for (unsigned long long i = rootStart; i<= rootEnd;i++)
	{

		unsigned long long pro = i*i;
		if ((pro>= inStart) && (pro<= inEnd))
		{
			if (isP(i))
			{
				if (isP(pro))
				{
					res++;
				}
			}

		}
	}

	printf("Case #%d: %d\n", test, res);
}

bool isP( unsigned long long a )
{
	stringstream ss;
	string s;
	ss << a;
	ss >> s;
	int len = s.length();
	if (len == 1)
	{
		return true;
	}
	else
	{
		int loop = len/2;
		for (int j = 0; j < loop ; j++)
		{
			char tmp = s[j];
			if (s[j] != s[len-1-j])
			{
				return false;
			}
		}
		return true;
	}
}
