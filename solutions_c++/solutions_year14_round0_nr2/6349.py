#include <iostream>
#include <cstdio>
using namespace std;

double C , F , X ;
#define eps (1e-6)

double solve (){
	double cur_time = X / 2.0;
	double rate = 2;
	double farm_time = 0 ;
	while ( true ){
		double temp = C/rate;
		farm_time += temp ;
		rate += F;
		double new_time = farm_time + X / rate;
		if ( new_time >  cur_time ){
			return cur_time ;
		}
		cur_time = new_time ;
	} 
}
int main (){
	int tc;
	cin >> tc;
	for ( int CC=1;CC<=tc;CC++){
		cin >> C >> F >> X;
		double answer = solve ();
		printf ( "Case #%d: %.7lf\n" , CC,answer);
	}
}
