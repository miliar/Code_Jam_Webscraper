// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

#define MAXN 10020

int s[ MAXN ];
bool f[ MAXN];
int n,x;


void init(){
	cin >> n >> x;
	int i;
	for ( i = 1; i <= n; i ++ )
		scanf( "%d", &s[i] );
	sort( s+1, s+n+1 );
	memset( f, false, sizeof(f) );
}

void cal(){
	int i, j, k = 0;
	for ( i = n; i >= 1; i -- )
		if ( !f[i] ){
			for ( j = i-1; j >= 1; j -- )
				if ( !f[j] && s[i]+s[j] <= x ){
					f[j] = true;
					break;
				}
			k ++;
			f[i] = true;
		}

	cout << k << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "A-large.in", "r", stdin );
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

