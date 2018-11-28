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

void check( map< int, int > & ans )
{
	int m;
	sf("%d",&m);
	--m;
	for( int i = 0; i < 4; ++i )
	{
		for( int j = 0; j < 4; ++j )
		{
			int t;
			sf("%d",&t);
			if( i == m ) ans[t]++;
		}
	}
}

int main()
{
	int T;
	sf("%d",&T);
	fr(ca,0,T)
	{
		map< int, int > ft;
		check(ft);
		check(ft);

	
		int ans = 0;
		for( map< int, int > :: iterator iter = ft.begin();  iter != ft.end(); ++iter )
		{
			if( iter->second > 1 )
			{
				if( ans ) ans = -1;
				else ans = iter->first;
			}
		}

		printf("Case #%d: ",ca + 1 );

		if( ans == 0 )
		{
			printf("Volunteer cheated!\n");
		}
		else if( ans == -1 )
		{
			printf("Bad magician!\n");
		}
		else
		{
			printf("%d\n",ans);
		}
	}
}
