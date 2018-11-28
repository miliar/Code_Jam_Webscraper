// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

#define MAXN 1010

char s[ MAXN ];
int n;

void init(){
	scanf( "%d %s", &n, s );
}

void cal(){
	int total = 0, si, ans = 0;
	for ( int i = 0; i <= n; i++ ){
		si = s[i]-'0';
		if ( si > 0 && total < i ){
			ans += i-total;
			total += ans;
		}
		total += si;
	}
	cout << ans << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "A-small-attempt2.in", "r", stdin );
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

