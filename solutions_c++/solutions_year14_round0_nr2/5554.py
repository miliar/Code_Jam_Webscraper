#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct Cookie{
	long double c, f, x;
	long double cookies = 0.0;
	unsigned farms = 0;
	long double time = 0.0;
	Cookie(){ cin >> c >> f >> x; }
	
	long double production( unsigned extra=0 ){ return 2 + f*(farms+extra); }
	long double timeFor( long double amount, unsigned extra=0 ){ return amount / production( extra ); }
	void buyFarm(){
		time += timeFor( c-cookies );
		farms++;
		cookies = 0;
	}
	
	long double result(){
		while( true ){
			if( timeFor( c-cookies ) + timeFor( x, 1 ) < timeFor( x-cookies ) )
				buyFarm();
			else{
				auto wait = timeFor( x-cookies, 0 );
				cookies += wait * production();
				return time + wait;
			}
		}
	}
};

int main( int, char** ){
	int amount;
	cin >> amount;
	cout.precision(17);
	for( int i=1; i<=amount; i++ )
		cout << "Case #" << i << ": " << Cookie().result() << endl;
	
	return 0;
}