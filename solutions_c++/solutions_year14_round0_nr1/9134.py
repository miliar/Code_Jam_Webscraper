#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <cstring>

using namespace std ;

#define vi vector<int>
#define vvi vector< vi >

vvi cards1 ;
vvi cards2 ; 
int arr[ 18 ] ; 

int frow ;
int srow ; 
int resu ;

void getIt( int &row , int id ) {
	cin >> row ; 
	
	vvi cards = vvi ( 4 , vi ( 4 , 0 ) ) ;
	
	for( int i = 0 ; i < 4 ; i ++ ) {
		for( int j = 0 ; j < 4 ; j ++ ) {
			cin >> cards[ i ][ j ] ; 
		}
	} 
	
	if( id == 1 ) {
		cards1 = cards ;
	}
	
	else {
		cards2 = cards ; 
	}
}

void input( int id ) {
	cards1.clear() ;
	cards2.clear() ;
	
	cards1 = vvi ( 4 , vi( 4 , 0 ) ) ;
	cards2 = vvi ( 4 , vi ( 4 , 0 ) ) ;
	
	cin >> frow ;
	frow -- ; 
	for( int i = 0 ; i < 4 ; i ++ ) {
		for( int j = 0 ; j < 4 ; j ++ ) {
			cin >> cards1[ i ][ j ] ; 
		}
	}
	
	cin >> srow ; 
	srow -- ;
	for( int i = 0 ; i < 4 ; i ++ ) {
		for( int j = 0 ; j < 4 ; j ++ ) {
			cin >> cards2[ i ][ j ] ; 
		}
	}
	
	/*
	if( id == 1 ) {
		getIt( frow , id ) ; 
		frow -- ;
	}
	
	else {
		getIt( srow , id ) ; 
		srow -- ; 
	}
	*/
//	cerr << frow << " ---- " << srow << endl ; 
}

int solve() {
	memset( arr , 0 , sizeof( arr ) ) ; 
	set<int> s ; 
//	cerr << "rows are " << frow << " " << srow << endl ; 	
	for( int i = 0 ; i < 4 ; i ++ ) {
//		cerr << cards1[ frow ][ i ] << " why dfdfd " << cards2[ srow ][ i ] << endl ;
		s.insert( cards1[ frow ][ i ] ) ; 
		s.insert( cards2[ srow ][ i ] ) ; 
	}
	
	if( s.size() == 7 ) {
		for( int i = 0 ; i < 4 ; i ++ ) {
			arr[ cards1[ frow ][ i ] ] ++ ;
			arr[ cards2[ srow ][ i ] ] ++ ; 
		}
		
		for( int i = 1 ; i <= 16 ; i ++ ) {
			if( arr[ i ] == 2 ) {
				resu = i ; 
			}
		}
	}
//	cerr << " dfdlfd " << 8 - (int)s.size() << endl ; 
	return 8 - (int)s.size() ; 
	
}

void printRes( int res , int cas) {
	if( res == 1 ) {
		cout << "Case #" << cas << ": " << resu << endl ; 
	}
	
	else if( res > 1 ) {
		cout << "Case #" << cas << ": Bad magician!" << endl ;  
	}	
	
	else {
		cout << "Case #" << cas << ": Volunteer cheated!" << endl ; 
	}
}

int main() {
	
	int T ; 
	
	cin >> T ; 
	
	for( int i = 0 ; i < T ; i ++ ) {
		input( 1 ) ; 
//		input( 1 ) ; 
//		input( 2 ) ; 
		
		int res = solve() ; 
		
		printRes( res , i + 1 ) ; 
	}
	
	return 0 ; 
}
