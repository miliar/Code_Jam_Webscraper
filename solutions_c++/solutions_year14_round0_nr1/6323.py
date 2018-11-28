
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <utility>
#include <iomanip>
using namespace std;


#define ll long long
#define rep(i,a,b) for(ll i = a;i<b;i++)
#define rev(i,a,b) for(ll i = (b-1); i>=a;i-- )
#define sl(a) scanf("%lld",&a)
#define sll(a,b) scanf("%lld%lld",&a,&b)
#define slll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define sllll(a,b,c,d) scanf("%lld%lld%lld%lld",&a,&b,&c,&d)
#define MOD 1000000007

int main()
{
	ll test;
	sl(test);
	rep(tt,1,test+1)
	{
		ll fa,sa,t;
		set<ll> chosen, ans;
		sl(fa);
		rep(i,0,4)
		{
			rep(j,0,4)
			{
				sl(t);
				if(i+1==fa)
					chosen.insert(t);
			}
		}
		sl(sa);
		rep(i,0,4)
		{
			rep(j,0,4)
			{
				sl(t);
				if(i+1==sa)
				{
					if(chosen.count(t)) ans.insert(t);
				}
			}
		}
		if(ans.size()==1)
		{
			printf("Case #%lld: %lld\n",tt,*(ans.begin()) );
		}
		else if(ans.size()>1)
		{
			printf("Case #%lld: Bad magician!\n",tt);
		}
		else
		{
			printf("Case #%lld: Volunteer cheated!\n",tt);
		}
	}
	return 0;
}