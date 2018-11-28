
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <unordered_map>


using namespace std;

int win( int n, long long p, long long k)
{
	if (p == 0)
		return 0;
	long long pl = 1;
		for (int i = 1; i<= n; i++)
			pl *= 2;
	long long better = k;
	long long worse = pl-k-1;
	while (pl > p)
	{
		// new round better kill each other, worse survive

		worse = worse-1;
		if (worse < 0)
			return 0;
		if (better % 2 == 0)
		{
			better = better/2;
			//worse = pl/2 - better - 1;
			worse = worse/2;
		}
		else
		{
			worse--;
			better = (better-1)/2 + 1;
			//worse = pl/2 - better - 1;
			worse = worse/2;
		}
		if (better < 0)
			return 0;
		if (worse < 0)
			return 0;
		pl = pl/2;
	}
	
	return 1;
}


int win2( int n, long long p, long long k)
{
	if (p == 0)
		return 0;
	if (k == 0 )
		return 1;
	long long pl = 1;
		for (int i = 1; i<= n; i++)
			pl *= 2;
	long long better = k;
	long long worse = pl-k-1;
	while (pl > p)
	{
		if (better == 0)
			return 1;
		// I lose
		long long rbetter = 1;
		// worse kill each other
		if (worse % 2 == 0)
		{
			worse = worse/2;
			better = pl/2 - worse - 1;
			//better = (better - 1)%2 + 1;
		}
		else
		{
			worse = (worse/2) +1;
			better = pl/2 - worse - 1;
			//better = (better-1-1)/2;
		}
		
		pl = pl/2;
		p = p-pl;
		if ( p <= 0)
			return 0;		
	}
	if (pl <= p)
		return 1;
	
	return 0;
}

int main()
{
	freopen("input.txt","rt", stdin);
	freopen("output.txt","wt", stdout);			
	int tests;
	scanf("%d\n", &tests);	
	long long pp = 1000002013;
	int o, e, p;
	map <int, long long> enter;
	map <int, long long> leave;
	map <int, long long> ind;

	long long sum [10000];
	map<int , long long> loc;
	//for (int i = 0; i < 3000; i++)
	for (int test = 1; test <= tests; test++)
	{

		long long p;
		int n;
		scanf("%d %I64d", &n, &p);		
		long long anw1 = 0;
		long long anw2 = 0;
			long long pl = 1;
		for (int i = 1; i<= n; i++)
			pl *= 2;
		long long l = 0;
		long long r = pl-1;
		// find max who can
		//for (int i = 0; i < 8; i++)
			//printf("%d ", win2(n, p, i));
		
		while (l < r)
		{
			long long m = ((l+r + 1)/2) ;
			if (win(n, p, m))
				l = m;
			else 
				r = m-1;
		}
		anw2 = l;

		l = 0;
		r = pl-1;
		// find max who can
		//for (int i = 0; i < 8; i++)
			//printf("%d ", win(n, p, i));

		win2(n, p, 2);
		while (l < r)
		{
			long long m = ((l+r +1)/2) ;
			if (win2(n, p, m))
				l = m;
			else 
				r = m-1;
		}

		anw1 = l;

		

		printf("Case #%d: %I64d %I64d\n",test, anw1, anw2);		

	}
		
	return 0;			
}     
