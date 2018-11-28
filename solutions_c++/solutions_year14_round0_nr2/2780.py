#include <set>
#include <map>
#include <queue>
#include <stack>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <limits.h>
#include <string.h>
#include <string>
#include <algorithm>
#define MID(x,y) ( ( x + y ) >> 1 )
#define L(x) ( x << 1 )
#define R(x) ( x << 1 | 1 )
#define FOR(i,s,t) for(int i=(s); i<(t); i++)
#define FORD(i,s,t) for(int i=(s-1); i>=t; i--)
#define BUG puts("here!!!")
#define STOP system("pause")
#define file_r(x) freopen(x, "r", stdin)
#define file_w(x) freopen(x, "w", stdout)

using namespace std;

int main() {
	int ncases;
	double c, f, x;
	
	file_r("B-large.in");
	file_w("out.txt");
	scanf("%d", &ncases);
	
	for(int ncase=1; ncase<=ncases; ncase++) {
		scanf("%lf%lf%lf", &c, &f, &x);
		double z = 2;
		double m = x / z;
		double t = 0;
		double p = m;
		while( 1 ) {
			t += c/z;
			z += f;
			if( t + x / z < m )
				m = t + x / z;
			if( t + x / z > m )
				break;
		//	cout << t <<' ' << z << endl;
		}
		printf("Case #%d: %.7lf\n", ncase, m);
	}
	return 0;
}

