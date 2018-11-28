// a.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>

using namespace std;


double c, f, x;

void init(){
	scanf( "%lf %lf %lf", &c, &f, &x );
}


void cal(){
	double t1, t2, t = 0.0, money = 2.0;
	
	t1 = x/money;
	t2 = x/(money+f) + c/money;

	while ( t1 >= t2 ){
		t += c/money;
		money += f;
		t1 = x/money;
		t2 = x/(money+f) + c/money;
	}
	t += t1;
	printf( "%.7lf\n", t );
}



int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "B-large.in", "r", stdin );
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

