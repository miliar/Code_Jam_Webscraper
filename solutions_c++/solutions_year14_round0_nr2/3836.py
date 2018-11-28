//============================================================================
// Name        : Google.cpp
// Author      : Anmol Ahuja
//============================================================================

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctype.h>
#include <cstdlib>
#include <climits>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for( int z=1; z<=t; ++z )
	{
		double c,f,x,time;
		scanf( "%lf %lf %lf", &c, &f, &x );
		int upper = floor( ((x*f) - (2*c))/(f*c) );
		upper = upper > 0 ? upper : 0;
		// printf("Upper: %d", upper);
		time = x/(2+(upper)*f);
		for( int i=0; i < upper ; ++i )
			time += c/(2 + i*f );
		printf( "Case #%d: %.7lf\n", z, time );
	}
	return 0;
}
