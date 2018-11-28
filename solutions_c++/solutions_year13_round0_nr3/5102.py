#include <iostream>
#include <string>
#include <vector>
#include <cstdio>

using namespace std;

int is_fair( int orgNumber ){
	int forward = orgNumber;
	int backward = 0;
	while( forward > 0 ){
		backward = backward * 10 + ( forward % 10 );
		forward = forward / 10;
	}

	if ( orgNumber == backward ){
		//cout << endl << "f=" << orgNumber;
		//cout << endl << "b=" << backward;
		return 1;
	} else {
		return 0;
	}
}

int is_square( int N ){
	double d_sqrt = sqrt( N );
	int i_sqrt = d_sqrt;
	if ( d_sqrt == i_sqrt ){
		return is_fair( i_sqrt );
	} else {
		return 0;
	}
}

int fair_and_square( int myA, int myB ){
	int cnt = 0;
	for( int x=myA; x<=myB; x++ ){
		if( is_square( x ) == 1 ){
			if( is_fair( x ) == 1 ){
				++cnt;
			}
		}
	}

	return cnt;
}

int main(){
	int T; cin >> T;

	vector< vector<int> > yard;

	for( int t=1; t<=T; t++ ){
		int myA; cin >> myA;
		int myB; cin >> myB;

		int out = fair_and_square( myA, myB );

		cout << "Case #" << t << ": " << out << endl;
	}
}