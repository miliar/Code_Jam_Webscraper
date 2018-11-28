
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
		long double c,f,x;
		scanf("%Lf %Lf %Lf",&c,&f,&x);
		long double r = 2;
		long double time_count = 0;
		while( (x/r) > ( (c/r) + (x/(r+f))  ) )
		{
			//buy farm
			time_count += c/r;
			r += f;
		}
		time_count += x/r;
		printf("Case #%lld: %.7Lf\n",tt, time_count);
	}
}