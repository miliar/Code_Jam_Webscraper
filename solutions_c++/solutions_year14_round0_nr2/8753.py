#include <cstdio>

using namespace std;

int T; 

double C, F, X;
double time_to_buy[100010];

inline void precompute() {

	double rate = 2; 
	
	time_to_buy[0] = 0;
	for ( int i = 1; i <= 100000; ++i ) {
		time_to_buy[i] = time_to_buy[i - 1] + C / rate;
		rate += F;
	}

}

void solve( int t ) {

	printf( "Case #%d: ", t );
	
	scanf( "%lf%lf%lf", &C, &F, &X );
	precompute();
	
	double sol = X;
	for ( int i = 0; i <= 100000; ++i ) {
		double time_to_win = time_to_buy[i] + X / (2 + (double) i * F);
		if (time_to_win < sol ) sol = time_to_win; else break;
	}
	
	printf( "%.7lf\n", sol );

}

int main( void ) {

	scanf( "%d", &T );
	for ( int i = 0; i < T; ++i ) solve( i + 1 );

	return 0;

}
