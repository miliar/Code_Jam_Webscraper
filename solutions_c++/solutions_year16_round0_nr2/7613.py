#include <bits/stdc++.h>

using namespace std ;
typedef long long ll;

int main() {
	
	freopen("in.txt","r",stdin) ;
	freopen("out.txt","w",stdout) ;
	
	int t ;
	cin >> t ;
	
	for( int k = 1 ; k <= t ; k++ ) {
		
		cout << "Case #" << k << ": " ;
		
		string str ;
		cin >> str ;
		char start ;
		start = str[0] ;
		
		int i = 1 , length = 1 ;
		while( str[i] ) {
			if( str[i] != str[i-1] ) length++ ;			
			i++ ;
		}
		
		if( start == '+' ) {
			if( length%2 ) cout << length-1 << endl ; 
			else cout << length << endl ;
			
		} else {
			if( length%2 ) cout << length << endl ; 
			else cout << length-1 << endl ;
		}
	}
	
	return 0 ;
}
