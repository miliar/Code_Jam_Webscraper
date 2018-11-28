# include <iostream>
# include <cstdio>
# include <string>

using namespace std ;

int main ( ) {
	ios_base::sync_with_stdio ( false ) ;
	int tc ; cin >> tc ;

	for ( int j = 1 ; j <= tc ; ++j ) {
		string a ; cin >> a ;
		int side , man=0 , i ;

		if ( a.at(0) == '+' )
			side = 1 ;

		for ( i = 1 ; i < a.size() ; ++i ) {
			if ( a.at(i) != a.at(i-1) ) {
				man += 1 ;
			}
		}

		if ( a.at(a.size()-1) == '-' )
			man += 1 ;

		printf ( "Case #%d: %d\n" , j , man ) ;

	}

	return 0 ;

}
