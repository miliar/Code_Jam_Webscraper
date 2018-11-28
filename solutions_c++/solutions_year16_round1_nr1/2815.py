# include <stdio.h>
# include <stdlib.h>
# include <iostream>
# include <algorithm>
# include <limits>
# include <math.h>
# include <string>

using namespace std;

# define MAX_INT numeric_limits<int>::max();
# define MAX_LONG numeric_limits<long long>::max();
# define MAX 2010

int main(){
	
	int T;

	string word , solution;
	cin >> T;
	for( int t = 1 ; t <= T ; t++ ){
		cin >> word;
		solution = "";
		for( int i = 0 ; i < word.size() ; i ++ ){

			if( solution == "" ){
				solution += word[ i ];
			}else if( solution[ 0 ] <= word[ i ] )
				solution = string( 1 , word[ i ] ) + solution;
			else
				solution += string( 1 , word[ i ] );

		}

		cout << "Case #" << t << ": " << solution << endl;
	}

	return 0;
}