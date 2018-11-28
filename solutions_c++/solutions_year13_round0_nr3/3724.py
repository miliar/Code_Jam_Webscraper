#include <iostream>
#include <math.h>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <limits.h>
#include <cstdio>

#include <utility>

#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;


bool pal( ll a )
{
	string s;
	while( a )
	{
		s += char( a%10 ) + '0';
		a /=10;
	}

	int si = s.size();
	int tmp = (s.size() + 1) / 2;

	for( int i = 0; i < tmp; i++ )
	{
		if( s[i] != s[si - i - 1] )
			return false;
	}

	return true;
}


void main()
{
	freopen( "C.in", "r", stdin );
	freopen( "C.out", "w", stdout );
	
	int tt;
	cin >> tt;


	for( int t= 0; t < tt; t++ )
	{

		ll a1,b1,a,b;

		cin >> a1 >> b1;

		a = (ll)sqrt( double(a1) ) - 1;
		if( a <= 0 ) a = 1;

		b = (ll)sqrt( double(b1) ) + 1;

		int res = 0;


		for( ll i = a; i < b; i++ )
		{
			if( pal(i) && (i*i <= b1 && i*i >= a1 ) && pal( i*i ) )
			{
				res++;
			}
		}
		
		cout << "Case #" << t+1 << ": " << res << endl;

	} // case

}

