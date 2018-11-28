#include <iostream>
#include <limits.h>
#include <string.h>
#include <queue>
#include <stdio.h>
#include <vector> 
#include <algorithm> 
#include <cmath>
#include <unistd.h>
#include <map>
#include <set>
using namespace std;
typedef pair<int,int> PII;

int main()
{
	int t;
	int tc=0;
	cin >> t;
	while(t--)
	{
		double minTimeRequired = 0.00000;
		double C,F,X;
		cin >> C >> F >> X;
		int itercount=0;
		long double timeToBuyFarm=C/(2.0+itercount*F);
		long double TimeToGetDeliciousCookies = X/(2.0+itercount*F);
		long double next_TimeToGetDeliciousCookies = X/(2.0+(itercount+1)*F);
		while(next_TimeToGetDeliciousCookies + timeToBuyFarm <= TimeToGetDeliciousCookies)
		{
			minTimeRequired += timeToBuyFarm;
			itercount++;
			timeToBuyFarm=C/(2.0+itercount*F);
			TimeToGetDeliciousCookies = X/(2.0+itercount*F);
			next_TimeToGetDeliciousCookies = X/(2.0+(itercount+1)*F);
		}
		minTimeRequired += TimeToGetDeliciousCookies;
		//cout.precision(7);
		printf("Case #%d: %.7lf\n", tc+1, minTimeRequired);
		tc++;
	}
	return 0;
}
