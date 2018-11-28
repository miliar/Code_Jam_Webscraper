#include <iostream>
#include <stdio.h>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include<string>
#include <fstream>
#include<iomanip>
#include<cstring>
using namespace std;
#define rep(i, x, y) for(int i = x; i < y; i++)
#define Rep(i, x, y) for(int i = x; i <= y; i++)
#define vi vector<int>
#define vvi vector<vector<int> >
#define pp push_back
typedef unsigned long long ull;

int main()
{
	//freopen( "input.in", "r", stdin );
	//freopen( "output.out", "w", stdout );
	int t, n, n1, arr1[ 5 ][ 5 ], arr2[ 5 ][ 5 ];
	scanf( "%d", &t );
	rep( i,1,t+1 )
	{
		scanf("%d", &n );
		rep( j,0,4 )
			rep( k,0,4 )
			scanf("%d", &arr1[ j ][ k ] );
		scanf("%d", &n1 );
		rep( j,0,4 )
			rep( k,0,4 )
			scanf("%d", &arr2[ j ][ k ] );
		n--; n1--;
		int ans = 0, chose = 0;
		if ( n >=0 && n <= 3 && n1 >=0 && n1 <= 3 )
		{
			rep( j,0,4 )
			{
				rep( k,0,4 )
				{
					if( arr1[ n ][ j ] == arr2[ n1 ][ k ] )
					{
						ans++;
						chose = arr1[ n ][ j ];
					}
				}
			}
		}
		printf( "Case #%d: ", i );
		if ( ans == 0 )
			puts("Volunteer cheated!");
		else if ( ans == 1 )
			printf( "%d\n", chose );
		else
			puts("Bad magician!");
	}
}