#include <iostream>
#include <assert.h>
#include <stack>
#include <algorithm>
#include <queue>

#include <math.h>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <string.h>
#include <string>
#include <stdio.h>
#define sf scanf
#define pf printf
#define ll long long

#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for(int i = a; i < b; ++i )
#define pb push_back 

using namespace std;


#define Max 10000000  

string id_num[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

int num[30];
int left_num = 0;
string ans;

int del( int index )
{
	string id = id_num[index];
	for( int i = 0; i < id.size(); ++i )
	{
		if( num[id[i]-'A'] <= 0 )
			return 0;
	}
	
	for( int i = 0; i < id.size(); ++i )
	{
		num[id[i]-'A']--; 
		left_num--;
	}
	return 1;
}

void rollback( int index )
{
	string id = id_num[index];
	for( int i = 0; i < id.size(); ++i )
	{
		num[id[i]-'A']++; 
		left_num++;
	}
}

int done()
{
	return left_num == 0;
}

int dfs( string ans )
{
	if( done() )
	{
		cout<<ans<<endl;
		return 1;
	}
	for( int i = 0; i < 10; ++i )
	{
		if( del(i) )
		{
			char x = i + '0';
			if( dfs( ans + x  ) )
			{
				return 1;
			}
			rollback( i );
		}
	}
	return 0;
}

string s;
void solve()
{
	left_num = 0;
	clr( num );
	for( int i =0; i < s.size(); ++i )
	{
		num[s[i]-'A']++;
		left_num++;
	}
	dfs("");
}

int main()
{
	int T;
	cin>>T;
	fr(c,0,T)
	{
		cin>>s;
		printf("Case #%d: ",c+1);
		solve();
	}
}
