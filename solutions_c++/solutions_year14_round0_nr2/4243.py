#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;

#define REP( i, N) for( int i = 0; (i < N); i ++ )
#define REP2( i , limit, N ) for( int i = limit; (i < N); i++ )

typedef vector<float> vi;
typedef vi::iterator vit;

int case_number;

void main2()
{
	double C, F, X;
	cin >> C;
	cin >> F;
	cin >> X;
	cout.precision( 7 );
	cout << "Case #" << ++case_number << ": ";

	if( X < C )
	{
		printf( "%.7f\n",  X / 2);
		return;
	}

	double earned = 0 ;
	double remaining = X - earned;
	double rate = 2;

	double time = 0;

	while( remaining > 0 )
	{
		double direct_time = remaining / rate;
		double farm_time = (C/rate) + ( remaining / (F+rate) );

		if( direct_time < farm_time )
		{
			remaining = 0;
			time += direct_time;
		}
		else
		{
			remaining = X;
			time += (C/rate);
			rate = rate + F;			
		}
	}

	printf( "%.7f\n", time );
}

int main ()
{
	int T;
	cin >> T;
	REP( i , T )
	{
		main2();
	}
}