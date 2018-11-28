#include <bits/stdc++.h>

using namespace std ; 

int giveNum( char shy ) {
	int res = shy - '0' ; 
	
	return res ;
}

int solve( int smax , string allshyness ) {
	int tot = 0 ; 
	int add = 0 ; 
	
	tot += giveNum( allshyness[ 0 ] ) ; 
	
	//cerr << tot << endl ; 	
	for( int i = 1 ; i < allshyness.size() ; i ++ ) {
		int curtot = giveNum( allshyness[ i ] ) ; 
		
		if( curtot == 0 ) continue ; 
		
		if( i > tot ) {
			add += ( i - tot ) ; 
			tot += ( i - tot ) ; 
			tot += curtot ; 
		}
		
		else {
			tot += curtot ; 
		}
	}
	
	return add ; 
}

int main() {
	
	int T ; 
	
	cin >> T ; 
	
	for( int i = 0 ; i < T ; i ++ ) {
		int smax ; 
		string allshyness = "" ; 
		
		cin >> smax ; 
		cin >> allshyness ; 
		
		int res = solve( smax , allshyness ) ; 
		cout << "Case #" << i + 1 << ": " << res << "\n" ; 
	}
	
	return 0 ; 
}
