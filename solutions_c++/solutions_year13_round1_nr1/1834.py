#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>
#include <cmath>
#include <math.h>
using namespace std;

int main()
{
	int T;
	long long r,t;
	scanf("%d",&T);
	for (int cs=1;cs<=T;cs++)
	{
		scanf("%lld%lld",&r,&t);
		long long ans = (-(2*r-1)+sqrt(1.0*(2*r-1)*(2*r-1)+8*t))/4;
		printf("Case #%d: %lld\n",cs,ans);
	}
	return 0;
}