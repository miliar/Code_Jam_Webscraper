# include <stdlib.h>
# include <stdio.h>
# include <algorithm>
# include <iostream>

using namespace std;

int main(){
	
	long long T , N , count , temp , mult;
	bool Found[ 10 ];

	cin >> T;
	for( int t = 1 ; t <= T ; t++ ){

		cin >> N;
		if( N == 0 ){
			cout << "Case #"<< t <<": INSOMNIA" << endl;
			continue;
		}

		count = 0 , mult = 1;
		fill( Found , Found + 10 , 0 );

		while( count < 10 ){

			temp = N * mult;
			while( temp > 0 ){

				if( !Found[ temp % 10 ] ){
					Found[ temp % 10 ] = true;
					count ++;
				}

				temp /= 10;
			}

			mult ++;
		}

		mult -- ;

		cout << "Case #"<< t <<": " << mult* N << endl;		
	}

	return 0;
}
