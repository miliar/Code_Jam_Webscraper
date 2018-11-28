#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <sstream>

using namespace std;

double arrA[1001];
double arrB[1001];

int main (int argc, char const* argv[])
{
	int T;
	scanf("%d",&T);
	
	for (int t = 1; t <= T; t += 1)
	{
		int n;
		scanf("%d",&n);
		
		for (int i = 0; i < n; i += 1)
		{
			scanf("%lf",&arrA[i]);
		}
		
		for (int i = 0; i < n; i += 1)
		{
			scanf("%lf",&arrB[i]);
		}
		
		sort(arrA,arrA+n,greater<double>());
		sort(arrB,arrB+n,greater<double>());
		
		int y = 0;
		int z = 0;

		int nl = 0;
		int kl = 0;
		
		for (int i = 0; i < n; i += 1)
		{
			if (arrA[nl] > arrB[kl])
			{	
				++y;
				++nl;
				++kl;
			}
			else
			{
				++kl;
			}
		}
		
		nl = 0;
		kl = 0;
		
		for (int i = 0; i < n; i += 1)
		{
			if (arrA[nl] > arrB[kl])
			{	
				++z;
				++nl;
			}
			else
			{
				++nl;
				++kl;
			}
		}
		
		printf("Case #%d: %d %d\n",t,y,z);
	}
	return 0;
}
