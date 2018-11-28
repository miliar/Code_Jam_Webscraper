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


int n,m;

int f[200][200];



bool checkRow( int _row, int _val )
{
	for( int i = 0; i < m ; i++ )	
	{
		if( f[_row][i] > _val )
			return false;
	}

	return true;
}

bool checkCol( int _col, int _val )
{
	for( int i = 0; i < n ; i++ )	
	{
		if( f[i][_col] > _val )
			return false;
	}

	return true;
}



void main()
{
	freopen( "B1.in", "r", stdin );
	freopen( "B1.out", "w", stdout );
	int tt;
	cin >> tt;

	bool fl = false;

	vector< int > len;

	for( int t= 0; t < tt; t++ )
	{

		fl = false;

		cin >> n >> m;
		for( int i = 0; i < n; i++ )
		for( int j = 0; j < m; j++ )
		{
			cin >> f[i][j];
		}


		for( int i = 0; i < n; i++ )
		{
			if( !fl )
				for( int j = 0; j < m; j++ )
				{
					if( !checkRow( i, f[i][j] ) && !checkCol( j, f[i][j] ) )
					{
						cout << "Case #"<< t+1 << ": " "NO" << endl;
						fl = true;
						break;
					}

				}
			else
				break;

		}

		if( !fl )
			cout << "Case #"<< t+1 << ": " "YES" << endl;


	} // case

}

