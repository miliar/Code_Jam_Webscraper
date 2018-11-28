#include<bits/stdc++.h>
using namespace std ;

int main() {

	freopen("in.txt","r",stdin) ;
	freopen("out.txt","w",stdout) ;
	int t , n ;
	string str ;
	cin >> t ;
	for( int k = 1 ; k <= t ; k++ ) {
		cin >> n >> str ;
		int counter = 0 , sum = 0 ;
		if( str[0] == '0' ) sum++ , counter++ ;
        sum += str[0]-48 ;
		for( int i = 1 ; i <= n ; i++ ) {
			if( sum < i )
				sum++ , counter++ ;
            sum += ( str[i]-48) ;
		}

		cout << "Case #" << k << ": " << counter << endl ;

	}
	return 0 ;

}
