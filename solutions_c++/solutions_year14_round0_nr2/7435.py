//shashwat001

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

#define INF 2147483647
#define LINF 9223372036854775807
#define mp make_pair
#define pb push_back

typedef long long int lli;
typedef pair<int,int> pi;

int main ()
{
	int t;
	scanf("%d",&t);
	for (unsigned int T = 1; T <= t; T += 1)
	{
		double c,f,x,time = 0;
		scanf("%lf %lf %lf",&c,&f,&x);
		double cur = 2;
		while(1)
		{
			double reqtime = x/cur;
			double reqbyfarm = c/cur + (x)/(cur+f);
			if(reqtime > reqbyfarm)
			{
				time += c/cur;
				cur+=f;
			}
			else
			{
				time += reqtime;
				break;
			}
		}
		printf("Case #%d: %lf\n",T,time);
	}
	return 0;
}
