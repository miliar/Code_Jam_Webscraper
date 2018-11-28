// a.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

#define MAXN 1010
double a[ MAXN ], b[ MAXN ];
int n;


void init(){
	cin >> n;
	int i;
	for ( i = 1; i <= n; i ++ )
		scanf( "%lf", &a[i] );
	for ( i = 1; i <= n; i ++ )
		scanf( "%lf", &b[i] );
	sort( a+1, a+n+1);
	sort( b+1, b+n+1 );
}


void cal(){
	int i, j, s = 0, c;
	j = 1;
	for ( i = 1; i <= n; i ++ )
		if ( a[i] > b[j] ){
			s++;
			j++;
		}
	cout << s << " ";

	s = 0;
	for ( i = 1; i <= n; i ++ ){
		c = 0;
		for ( j = 1; j <= n; j ++ )
			if ( b[j] > a[i] ){
				c = j;
				break;
			}
		if ( c > 0 ){
			b[c] = 0;
			s ++;
		}
		else{
			break;
		}
	}
	s = n-s;
	cout << s << " " << endl;
}



int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "D-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t, i;
	scanf( "%d\n", &t );
	for ( i = 1; i <= t; i ++ ){
		init();
		cout << "Case #" << i << ": ";
		cal();
	}
	return 0;
}

