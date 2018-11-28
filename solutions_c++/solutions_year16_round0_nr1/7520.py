#include <bits/stdc++.h>

using namespace std ;
typedef long long ll;

ll calculateNumber(ll num) {
	
	//cout << "num : " << num << endl ;
	int status[10] ;
	for( int i= 0 ; i < 10 ; i++ ) status[i] = 0 ;
	ll temp = num , cur ;
	int loopCounter = 0 ;
	
	while( 1 ) {
		int counter = 0 ;
		
		cur = temp ;
		while( temp ) {
			status[ temp%10 ]++ ;
			temp /= 10 ;
		}
		for( int i = 0 ; i < 10 ; i++ ) if( status[i] ) counter++ ;
		//cout << "counter : " << counter << " & cur : " << cur << endl ;
		if( counter == 10 ) return cur ;
		temp = cur+num ;
		
	//	loopCounter++ ;
	//	if( loopCounter > 1000 ) return -1 ;
 	}
}

int main() {
	
	freopen("in.txt","r",stdin) ;
	freopen("out.txt","w",stdout) ;
	
	int t ;
	ll num ;
	cin >> t ;
	for( int k = 1 ; k <= t ; k++ ) {
		cin >> num ;
		cout << "Case #" << k << ": " ;
		
		if( num )
			cout << calculateNumber(num) << endl ;
		else cout << "INSOMNIA" << endl ;
	}
	
	return 0 ;
}
