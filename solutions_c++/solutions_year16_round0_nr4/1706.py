#include <bits/stdc++.h>

using namespace std ; 

void printRes( int cas , vector<int> res ) {
	cout << "Case #" << cas << ":" ;
	
	for( int i = 0 ; i < res.size() ; i ++ ) {
		cout << " " << res[ i ] ; 
	}
	cout << endl ; 
}

int main() {
	
	int T ; 
	
	cin >> T ; 
	
	for( int i = 0 ; i < T ; i ++ ) {
		int K , C , S ; 
		cin >> K >> C >> S ; 
		
		vector<int> res ; 
		
		for( int j = 1 ; j <= S ; j ++ ) {
			res.push_back( j ) ; 
		}
		
		printRes( i + 1 , res ) ; 
	}
	return 0 ; 
}
