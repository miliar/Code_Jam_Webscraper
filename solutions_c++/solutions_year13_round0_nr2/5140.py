//============================================================================
// Name        : LawnMower.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#define MAX 100
using namespace std;

bool isPossible( int lawn[MAX][MAX], int m, int n )
{
	int maxR[MAX], maxC[MAX];
	for( int i=0; i<n; ++i)
	{
		maxR[i]=lawn[i][0];
		for( int j=1; j<m; ++j)
			if( maxR[i]<lawn[i][j] )
				maxR[i]=lawn[i][j];
	}
	for( int i=0; i<m; ++i)
	{
		maxC[i]=lawn[0][i];
		for( int j=1; j<n; ++j)
			if( maxC[i]<lawn[j][i] )
				maxC[i]=lawn[j][i];
	}
	for( int i=0; i<n; ++i)
	{
		for(int j=0; j<m; ++j)
		{
			if( lawn[i][j]!=maxR[i] && lawn[i][j]!=maxC[j] )
				return false;
		}
	}
	return true;
}
int main() {
	int t,x;
	int m , n, lawn[MAX][MAX];
	scanf("%d",&t);
	for( x=1; x<=t; ++x)
	{
		scanf("%d %d", &n, &m);
		for( int i=0; i<n; ++i )
			for( int j=0; j<m; ++j)
				cin>>lawn[i][j];

		printf( "Case #%d: %s\n", x, isPossible( lawn, m ,n )?"YES":"NO" );
	}
	return 0;
}
