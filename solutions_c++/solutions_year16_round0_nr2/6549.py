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

int n;
int a[10000000];

void reserve( int s, int e )
{
	//printf("s = %d e = %d\n",s,e);
	while( s < e )
	{
		swap(a[s], a[e]);
		a[s] ^= 1;
		a[e] ^= 1;
		s++;
		e--;
	}
	if( s == e )
	{
		a[s] ^= 1;
	}
}

int reserve( int index )
{
	/*
	printf("index = %d\n",index);
	for( int i = 0; i < n; ++i )
		printf("%d ",a[i]);
	printf("\n");
	*/

	for( int i = 0; i <= index; ++i )
	{
		if( a[i] == 0 )
		{
			if( i > 0 )
			{
				reserve(0,i-1);
				reserve(0,index);
				return 2;
			}
			else
			{
				reserve(0,index);
				return 1;
			}
		}
	}
	reserve(0,index);
	return 1;
}

int real_solve()
{
	int num = 0;
	while( 1 )
	{
		int id = -1;
		for( int i = n-1; i >=0; --i )
		{
			if( a[i] == 0 )
			{
				id = i;
				break;
			}
		}
		if( id == -1 ) 
			break;

		num+=reserve( id );
	
		/*
		printf("id = %d\n",id);
		for( int i = 0; i < n; ++i )
			printf("%d ",a[i]);
		printf("\n");
		*/
	}
	return num;
}

string str;
int solve()
{
	for( int i = 0; i < str.size();++i )
	{
		if( str[i] == '-' ) a[i] =0;
		else a[i] = 1;
	}
	n = str.size();
	return real_solve();
}

int main()
{
	int T;
	cin>>T;
	fr(c,0,T)
	{
		cin>>str;
		printf("Case #%d: %d\n",c+1,solve());
	}
}
