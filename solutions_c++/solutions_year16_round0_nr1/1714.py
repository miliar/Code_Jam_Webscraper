#include <bits/stdc++.h>

using namespace std ; 

void printRes( int cas , long long res ) {

	if( res == -1 ) {
		cout << "Case #"<<cas<<": INSOMNIA" << endl;
	}
	else {
		cout << "Case #"<<cas<<": " << res << endl ; 
	}
}

long long solve( long long N ) {
	if( N == 0 ) return -1 ; 
	
	set<int> s ; 
	
	int org = N ; 
	
	while( true ) {
		ostringstream oss ; 
		oss << N ; 
		string cur = oss.str() ; 
		
		for( int i = 0 ; i < cur.size() ; i ++ ) {
			int dig = cur[ i ] - '0' ; 
			s.insert( dig ) ; 
		}
		
		if( s.size() == 10 ) return N ; 
		N += org ; 
	} 
}

int main() {
	
	int T ; 
	
	cin >> T ; 
	
	for( int i = 0 ; i < T ; i ++ ) {
		int N ; 
		cin >> N ; 
		long long res = solve( N ) ; 
		printRes( i + 1 , res ) ; 	
	}
	
	return 0 ; 
}
