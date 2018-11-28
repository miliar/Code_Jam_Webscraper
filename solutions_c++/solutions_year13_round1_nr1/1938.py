// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

#define SQR(a) ((a)*(a))

double const PI = acos(double(-1));
int r, t;


void init(){
	cin >> r >> t;
}

void cal(){
	int x = 0;
	do{
		t -= ( SQR(r+1)-SQR(r) );
		r += 2;
		if ( t >= 0 )
			x += 1;
	}while (t>0);
	cout << x << endl;
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

