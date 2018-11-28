#include <iostream>
#include <fstream>
#include <iomanip>
#include <float.h>

long double min;

long double recur ( long double C , long double F , long double X , int nf , long double c , long double t ) {

	long double z;
	if ( C < X && c < C )
		z = C - c;
	else
		z = X - c;
	c += z;
	t += (z/(2+nf*F));
	if ( t >= min )
		return DBL_MAX;
	if ( c == X ) {
		min = t;
		return t;
	}
	long double a = recur ( C,F,X,nf,c,t);
	long double b = DBL_MAX;
	if ( c == C && t < X/2 )
		b = recur ( C,F,X,nf+1,0,t );
	return a < b ? a : b;
}

int main () {

	std::ifstream input ( "input.txt" );
	std::ofstream output ( "output.txt" );
	int T;
	long double C,F,X,t;
	input >> T;
	for ( int i = 0 ; i < T ; ++i ) {

		min = DBL_MAX;
		input >> C >> F >> X;
		t = recur(C,F,X,0,0,0);
		output << "Case #" << i+1 << ": " << std::fixed << std::setprecision(7) << t << std::endl;
	}
	return 0;
}
