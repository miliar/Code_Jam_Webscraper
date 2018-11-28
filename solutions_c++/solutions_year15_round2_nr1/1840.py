#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <cmath>
#include <algorithm>
#include <deque>
#include <map>
#include <utility>
#include <cstdio>
using namespace std;

const int MAXSIZE = 1000003;
int din[MAXSIZE];


long long  reverse(long long n)
{
	long long res =  0;


	while(n > 0)
	{
		res *= 10;
		res += n%10;
		n/= 10;

	}
	return res;
}








void init();


int main()
{
	init();

#ifndef _DEBUG
	freopen("E:\\in.txt", "r", stdin);
	freopen("E:\\out.txt", "w", stdout);
#endif

	int t;
	cin >> t;
	for(int tt = 0; tt < t; tt++)
	{



		long long  n;
		cin >> n;

		int res =  din[n];

		printf("Case #%d: %d\n", tt+1, res);
	}


	return 0;

}

void init()
{

	for(int i = 1; i < MAXSIZE; i++)
	{
		din[i]  = 10000000;
	}
	din[1] = 1;
	for(int i = 1; i < MAXSIZE; i++)
	{
		long long r = reverse(i);
		if(r > MAXSIZE)
			continue;
		if(r > i)
		{
			din[r] = min(din[i] + 1, din[r]);
		}
		else
		{
			if(din[i] + 1 < din[r])
			{
				throw;
			}
		}
		din[i + 1] = min(din[i + 1], din[i] + 1);
	}
}