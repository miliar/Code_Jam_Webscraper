#include <stdio.h>

#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

#define ll long long
#define sf scanf
#define pf printf
#define pb push_back
#define clr(x) memset(x,0,sizeof(x))
#define fr(x,a,b) for(int x=a; x<b;++x)

string s[100];
int p[100];
int ans;
int ans_count;
int n,m;

int dp[10000];

void init()
{
	clr( dp );
	for( int i = 0; i < ( 1 << n ); ++i )
	{
		set< string > ft;
		for( int j = 0; ( 1 << j ) <= i; ++j )
		{
			if( i & ( 1 << j ) )
			{
				string x = s[j];
				string sb;
				for( int k = 0; k < x.size(); ++k )
				{
					sb += x[k];
					ft.insert( sb );
				}
			}
		}
		if( ft.size() ) ft.insert( "" );
		dp[i] = ft.size();
	}
}

void count()
{
	int sum = 0;
	for( int i = 0; i < m; ++i )
	{
		int nima = 0;
		for( int j = 0; j < n; ++j )
		{
			if( p[j] == i )
			{
				nima |= ( 1 << j );
			}
		}

		sum += dp[nima];

		/*

		set< string > ft;
		for( int j = 0; j < x.size(); ++j )
		{
			string sb = "";
			for( int k = 0; k < x[j].size(); ++k )
			{
				sb += x[j][k];
				ft.insert( sb );
			}
		}
		if( ft.size() ) ft.insert( "" );
		sum += ft.size();
		*/
	}

	if( ans < sum )
	{
		ans = sum;
		ans_count = 1;
	}
	else if( sum == ans )
	{
		++ans_count;
	}
}

void dfs(int x)
{
	if( x >= n )
	{
		count();
		return ;
	}
	for( int i = 0; i < m; ++i )
	{
		p[x] = i;
		dfs( x + 1 );
		p[x] = -1;
	}
}

int main()
{
	int T;
	sf("%d",&T);
	fr(ca,0,T)
	{

		sf("%d%d",&n,&m);
		fr(i,0,n)
		{
			cin>>s[i];
		}
		ans = 0;
		ans_count = 0;

		init();

		dfs( 0 );

		pf("Case #%d: %d %d\n",ca+1, ans,ans_count );
	}
}
