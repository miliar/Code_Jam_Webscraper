#include <stdio.h>
#include<stdio.h>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<set>
#include<iostream>
#include<string.h>
#include<sstream>
#include<math.h>

using namespace std;

#define SZ(x) x.size()
#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for( int i = a; i < b; ++i )
#define frr(i,a,b) for( int i = a; i > b; --i )

#define pb push_back
#define mp make_pair
#define pf printf
#define sf scanf

#define ll long long

int main()
{
	int T;
	sf("%d",&T);
	fr(ca,0,T)
	{
		double c,f,x;
		sf("%lf%lf%lf",&c,&f,&x);

		double ans = 0;
		for( int i = 0; ; ++i )
		{
			double x1 = x/(2.0+i*f);
			double x2 = x/(2.0+(i+1)*f);
			double x3 = c/(2.0+i*f);

			if( x1 <= x2 + x3 )
			{
				ans += x1;
				break;
			}


			ans += x3;
		}

		printf("Case #%d: %.7lf\n",ca + 1, ans );
	}
}
