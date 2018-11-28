# include <stdio.h>
# include <stdlib.h>
# include <iostream>
# include <algorithm>
# include <string>

using namespace std;

int main(){
	
	int T , count , pos;
	string stack;
	cin >> T;
	for( int t = 1 ; t <= T ; t++ ){

		cin >> stack;
		count = 0;

		for( int i = stack.size() - 1 ; i >= 0 ; i-- ){

			if( stack[ i ] == '-' ){

				pos = 0;
				while( stack[ pos ] == '+' ){
					stack[ pos ] = '-'; pos ++; 
				}

				if( pos > 0 ) count++;

				for( int j = 0 ; j <= i ; j++ )
					stack[ j ] = stack[ j ] == '+' ? '-' : '+';

				reverse( stack.begin() , stack.begin() + i + 1 );

				count ++;

			}

		}

		cout << "Case #"<< t <<": "<< count << endl;

	}

	return 0;
}