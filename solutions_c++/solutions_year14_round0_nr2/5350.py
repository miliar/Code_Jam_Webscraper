#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include<set>
#include <map>
#include <time.h>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for(int cas = 1; cas<=t; ++cas)
	{
		double c,f,x;
		cin>>c>>f>>x;
		vector<double> dp(int(x)+10,0);
		double total = 1e18;

		for(int i=0; i<(int)x; ++i)
		{
			double persec = 2 + i*f;
			total = min(total, dp[i]+x/persec);
			dp[i+1] = dp[i]+c/persec;
		}
		printf("Case #%d: %.7lf\n", cas, total);
	}
	return 0;
}