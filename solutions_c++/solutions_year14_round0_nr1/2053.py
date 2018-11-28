// a.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>

using namespace std;

#define MAXN 10

int a[2][MAXN];


void init(){
	int k, j, i, c, num;
	for ( k = 0; k <= 1; k ++ ){
		scanf( "%d", &c );
		for ( i = 1; i <= 4; i ++ )
			for ( j = 1; j <= 4; j ++ ){
				scanf( "%d", &num );
				if ( i == c )
					a[k][j] = num;
			}
	}
}


void cal(){
	int i, j, c, f;
	c = 0;
	for ( i = 1; i <= 4; i ++ )
		for ( j = 1; j <= 4; j ++ )
			if ( a[0][i] == a[1][j] ){
				c++;
				f = a[0][i];
			}
	switch (c){
		case 1:
			cout << f << endl;
			break;
		case 0:
			cout << "Volunteer cheated!" << endl;
			break;
		default : cout << "Bad magician!" << endl;
	}	
}



int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "A-small-attempt0.in", "r", stdin );
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

