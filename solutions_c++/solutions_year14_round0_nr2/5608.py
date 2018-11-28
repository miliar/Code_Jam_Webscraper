#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<iostream>
#include<set>
#include<utility>
#include<algorithm>
using namespace std;

long double f(long double C, long double F, long double X)
{
	if( X <= C )
		return X / 2.0;

	long double t = 0,   // [s]   time
	            f = 2.0; // [C/s] current Cps
//	while( X / f > C / f + X / (f + F) ){ // buy one more farm?
	while( X * F > C * (f + F) ){ // buy one more farm?
		t += C / f;
		f += F;
	}
	t += X / f;
	return t;
}

int main()
{
	int T;
	cin >> T;
	for( int C = 1; C <= T; C ++ ){
		double CC, // [C]   price of a farm
		       F, // [C/s] benefit of a farm
		       X; // [C]   target amount of cookies
		cin >> CC >> F >> X;
		double t = (double)f(CC, F, X);
		printf( "Case #%d: %.10lf\n", C, t );
	}
}
