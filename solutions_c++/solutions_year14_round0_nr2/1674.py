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

int main (int argc, char const* argv[])
{
	int T;
	scanf("%d",&T);
	
	for (int t = 1; t <= T; t += 1)
	{
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		
		double time = 0;
		double rate = 2.0;
		double ans = x/rate;
		
		for (int i = 0; i < 1000000; i += 1)
		{
			time += c/rate;
			rate += f;
			
			ans = min(ans,time+x/rate);
		}
		
		printf("Case #%d: %.8lf\n",t,ans);
	}
	return 0;
}
