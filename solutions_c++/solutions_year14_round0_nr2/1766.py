#include <iostream>
#include <cstdio>
#include <cmath>

#define ld long double 
#define eps 10e-8

using namespace std;

int cmp(ld x, ld y) {
	if( fabs(x - y) < eps)
		return 0;
	if(x < y) 
		return -1;
	return 1;
}

bool F(ld T, ld X, ld C, ld F) {

	ld v = 2.0;
	ld t = 0.0;

	while(1) {

		if( cmp (v * (T - t) , X) != -1 )
			return true;

		ld aux = C / v;

		t += aux;
		v += F;

		if( cmp (t, T) == 1)
			return false;
	}
}

ld search(ld c, ld f, ld x) {
	ld beg = 0.0;
	ld end = (x/2.0) + 1;
	ld mid;

	while( cmp (beg , end) != 0) {

		mid = (end + beg)/2;

		if(F(mid, x, c, f)) 
			end = mid ;
		else 
			beg = mid;
	}

	return end;
}

int main( int argc, char ** argv)
{
	ios::sync_with_stdio(NULL);
	int t;
	ld c, f, x;

	cin >> t;
	for(int i = 1; i <= t; i++) {
		cin >> c >> f >> x;

		printf("Case #%d: ", i);

		printf("%.7Lf\n", search(c, f, x));
	}

	return 0;
}
