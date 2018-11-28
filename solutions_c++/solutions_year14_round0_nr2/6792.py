#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

#define T_MAX 100
#define V 2
#define C_MAX 500
#define F_MAX 4
#define X_MAX 2000

double MinTime( double C, double F, double X )
{
	double time;
	double ntime = X / 2;
	int n;
	for ( n = 1; ; n++ )
	{
		time = ntime;
		ntime = ntime - X / (2+F*(n-1)) + C / ( 2+F*(n-1) ) + X / (2+F*n);
		if ( ntime > time ) return time;
	}
}

void main()
{
	ifstream fin( "B-large.in" );
	ofstream fout( "B-large.out" );
	int T;
	fin>>T;

	double C, F, X, mint;
	int t;
	for ( t = 0; t < T; t++ )
	{
		fin>>C>>F>>X;
		mint = MinTime( C, F, X );
		fout<<"Case #"<<t+1<<": ";
		fout<<fixed<<setprecision(7)<<mint<<endl;
	}	
}
