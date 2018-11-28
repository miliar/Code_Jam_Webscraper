#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <cctype>
#include <cstdio>
#include <memory>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>

#define sqr(x) ((x) * (x))
#define minn(x,y) (x=(y)<(x)?(y):(x))
#define maxx(x,y) (x=(y)>(x)?(y):(x))
#define pluss(x,y) (x+=(y),x%=mod)
#define random(x) ((((rand()%32767)*(rand()%32767)*(rand()%32767)%(x))+(x))%(x))

using namespace std;

typedef	long long	int64;


int64	p[66], N, P, T;


int64	workHigh()
{
	int64	L = 1, R = T;
	
	while (L <= R)
	{
		int64	M = (L + R) >> 1;
		
		int64	S = M - 1, yes = 1;
		
		for (int i = 0; i < N && yes; ++ i)
		{
			if (p[i] == 1)
			{
				if (S > 0) yes = 0;
				break;
			}
			S = (S - 1) / 2;
		}
		
		if (yes) L = M + 1; else R = M - 1;
	}
	
	return R;
}

int64	workLow()
{
	int64	L = 1, R = T;
	
	while (L <= R)
	{
		int64	M = (L + R) >> 1;
		
		int64	S = T - M, yes = 1;
		
		for (int i = 0; i < N && yes; ++ i)
		{
			if (p[i] == 1)
			{
				if (S <= 0) yes = 0;
				S = (S - 1) / 2;
				continue;
			}
			if (S > 0)
			{
				yes = 1;
				break;
			}
		}
		
		if (yes) L = M + 1; else R = M - 1;
	}
	
	return R;
}

int	main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int	Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; ++ test)
	{
		scanf("%I64d%I64d", &N, &P);
		P -= 1;
		T = 1ll << N;
		for (int i = N - 1; i >= 0; -- i)
		{
			p[i] = 1 - P % 2;
			P /= 2;
		}
		
		int64	ansHigh = workHigh();
		int64	ansLow = workLow();
		printf("Case #%d: %I64d %I64d\n", test, ansHigh - 1, ansLow - 1);
	}
	
	return 0;
}
