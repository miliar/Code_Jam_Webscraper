#include <stdio.h>
#include <vector>
#include <sstream>
#include <iostream>
#include <math.h>
#include <string>
#include <map>

using namespace std;

#define sf scanf
#define pf printf
#define pb push_back
#define fr(x,a,b) for( int x = a; x < b; ++x )
#define clr(x) memset(x,0,sizeof(x));
#define ll long long

int check( ll x )
{
	ll m = x;
	ll t = 0;
	while( x > 0 )
	{
		t = t * 10 + x%10;
		x/=10;
	}
	return m == t;
}
vector< ll > ft;

int ct(int x)
{
	int num = 0;
	fr(i,0,ft.size())
	{
		if( ft[i] <= x )
			++num;
	}
	return num;
}

int main()
{
	fr(i,1,10000001)
	{
		if( check( i ) && check( (ll)i*i ) )
		{
			ft.pb((ll)i*i);
		}
	}

	int T;
	sf("%d",&T);
	fr(ca,0,T)
	{
		int l,r;
		sf("%d%d",&l,&r);
		pf("Case #%d: %d\n",ca+1,ct(r)-ct(l-1));	
	}
}
