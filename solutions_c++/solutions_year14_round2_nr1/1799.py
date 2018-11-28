
#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

#define fr( i , c , n ) for( int i = (c) ; i < (n) ;i++ )
#define clr( a , c ) memset( a , c , sizeof a )
#define P pair<int , int>
#define L  long long

#define maxn 102
string a[maxn];
int nr[maxn];
int ind[maxn];
int main()
{

	int T; scanf("%d" , &T );
	fr( t , 1 , T+1 )
	{
		int n; scanf("%d" , &n );
		cin.ignore();
		fr( i , 0 , n )
			getline( cin , a[i] );
		clr( ind , 0 );
		int ans = 0;
		bool ok = true;
		while( true )
		{
			clr( nr , -1 );//:D
			if( ind[0] >= a[0].size() )// avelie tamum shod
			{
				bool notfinished = false;
				fr( i , 0 , n )
					if( ind[i] < a[i].size() )
					{
						notfinished = true;
						break;
					}
				if( notfinished ) ok = false;
				break;
			}
			char c = a[0][ ind[0] ];
			int sum = 0;
			bool haveto = false;
			fr( i , 0 , n )
			{
				for( ; ind[i] < a[i].size() ; ind[i]++ )
					if( a[i][ind[i]] != c ) break;
					else nr[i] ++;

				if( nr[i] < 0 ) 
				{
					ok = false; break;
				}
				else if( nr[i] == 0 )
					haveto = true;
				else
					sum += nr[i];
			}
			if( !ok ) break;

			if( haveto )
				ans += sum;
			else
			{
				int mid = (int)((double) sum/n + 0.5 );
				fr( i , 0 , n )
					ans += abs( nr[i] - mid );
			}
			
		}

		if( ok )
			printf("Case #%d: %d\n" , t , ans );
		else
			printf("Case #%d: Fegla Won\n" , t );

	}
	return 0;
}