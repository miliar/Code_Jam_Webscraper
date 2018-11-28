#include <bits/stdc++.h>

using namespace std ; 

void printRes( int cas , int res ) {
	cout << "Case #" << cas << ": " << res << "\n" ; 
}

int solve( string line ) {
	vector<int> tmp ; 
	
	if( line[ 0 ] == '-' ) tmp.push_back( 0 ) ; 
	else tmp.push_back( 1 ) ; 
	
	for( int i = 1 ; i < line.size() ; i ++ ) {
		if( line[ i ] != line[ i - 1 ] ) {
			if( line[ i ] == '+' ) {
				tmp.push_back( 1 ) ; 
			}
			else tmp.push_back( 0 ) ; 
		}
	}
	
	if( tmp[ tmp.size() - 1 ] == 1 ) {
		vector<int> tt ; 
		for( int i = 0 ; i < ( tmp.size() - 1 ) ; i ++ ) {
			tt.push_back( tmp[ i ] ) ; 
		} 
		tmp = tt ; 
	}
	
	int tot = 0 ; 
	
	int st = 0 ; 
	
	if( tmp[ 0 ] == 0 ) {
		st = 1 ; 
		tot ++ ; 
	}
	
	for( int i = st ; i < tmp.size() ; i += 2 ) {
		tot += 2 ; 
	}
	
	return tot ; 
}

int main() {
	
	int T ; 
	
	cin >> T ; 
	
	for( int i = 0 ; i < T ; i ++ ) {
		string line = "" ; 
		
		cin >> line ; 
		
		int res = solve( line ) ; 
		printRes( i + 1 , res ) ; 
	}
	
	return 0 ; 
}
