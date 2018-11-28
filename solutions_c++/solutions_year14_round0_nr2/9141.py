#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std ;

double C , F , X ; 

double solve() {
	double mins = X / 2 ;
	
	double privTime = 0.0 ; 
	double curRate = 2 ; 
	
	for( int i = 0 ; i < X ; i ++ ) {
		double curTime = privTime + ( X / curRate ) ; 
		
		mins = min( mins , curTime ) ; 
		
		privTime = privTime + ( C / curRate ) ;
		curRate += F ;  
	}
	
	return mins ; 
}

int main() {
	
	int T ; 
	
	cin >> T ; 
	
	for( int i = 0 ; i < T ; i ++ ) {
		cin >> C >> F >> X ; 
		
		double res = solve() ; 
		
		cout << "Case #" << i + 1 <<": " ;
		printf("%.9lf\n",res) ; 
	}
	
	return 0 ; 
}
