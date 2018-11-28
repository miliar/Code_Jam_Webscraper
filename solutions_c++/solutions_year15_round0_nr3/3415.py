#include <bits/stdc++.h>

using namespace std ; 

int allrows  [][ 5 ] = { { 0 , 1 , 2 , 3 } , { 1 , 0 , 3 , 2 } , { 2 , 3 , 0 , 1 } , { 3 , 2 , 1 , 0 } } ; 
int allsigns [][ 5 ] = { { 1 , 1 , 1 , 1 } , { 1 , -1 , 1 , -1 } , { 1 , -1 , -1 , 1 } , { 1 , 1 , -1 , -1 } } ; 
int cache[ 10010 ] ; 
pair<int,int> fst ; 
pair<int,int> snd ;

int getRow( char ch ) {
	if( ch == 'i' ) return 1 ; 
	else if( ch == 'j' ) return 2 ; 
	else return 3 ;  
}

int getSign( int row , int col ) {
	return allsigns[ row ][ col ] ; 
}

int getNw( int row , int col ) {
	return allrows[ row ][ col ] ; 
}

bool ok1( int en , string & fin ) {
	
	if( en == 0 ) {
		fst.first = getRow( fin[ 0 ] ) ; 
		fst.second = 1 ; 
	}
	
	else {
		int col = getRow( fin[ en ] ) ;
		int nr = getNw( fst.first , col ) ;  
		int nsign = getSign( fst.first , col ) ; 
		
		fst.first = nr ; 
		fst.second = fst.second * nsign ; 
	}
	/*
	int sign = 1 ; 
	int row = getRow( fin[ 0 ] ) ; 
	*/
	/*
	for( int i = 1 ; i <= en ; i ++ ) {
		int col = getRow( fin[ i ] ) ; 
		int nr = getNw( row , col ) ; 
		int nsign = getSign( row , col ) ; 
		sign = ( sign * nsign ) ; 
		row = nr ; 
	}
	*/
	if( fst.first == 1 && fst.second == 1 ) return true ; 
	return false ; 
}

bool ok2( int st , int en , string & fin , bool isF ) {
	
	if( isF ) {
		snd.first = getRow( fin[ en ] ) ; 
		snd.second = 1 ; 	
	}
	
	else {
		int col = getRow( fin[ en ] ) ; 
		int nr = getNw( snd.first , col ) ; 
		int nsign = getSign( snd.first , col ) ; 
		
		snd.first = nr ; 
		snd.second = ( snd.second * nsign ) ; 
	}
	
	if( snd.first == 2 && snd.second == 1 ) return true ; 
	return false ; 
	/*
	int sign = 1 ; 
	int row = getRow( fin[ st ] ) ; 
	
	for( int i = st + 1 ; i <= en ; i ++ ) {
		int col = getRow( fin[ i ] ) ; 
		int nr = getNw( row , col ) ; 
		int nsign = getSign( row , col ) ; 
		sign = ( sign * nsign ) ; 
		row = nr ; 
	}
	
	if( row == 2 && sign == 1 ) return true ; 
	return false ; 
	*/
}

bool ok3( int ind , string &fin ) {
	if( ind >= fin.size() ) return false ; 
	if( cache[ ind ] != -1 ) {
		if( cache[ ind ] == 1 ) return true ; 
		return false ; 
	}
	
//	cerr << "here" << endl ;
	
	int sign = 1 ; 
	int row = getRow( fin[ ind ] ) ; 
	
//	cerr << sign << " " << row << endl ; 
	for( int i = ind + 1 ; i < fin.size() ; i ++ ) {
		int col = getRow( fin[ i ] ) ; 
		int nr = getNw( row , col ) ; 
		int nsign = getSign( row , col ) ; 
		sign = ( sign * nsign ) ; 
		row = nr ; 	
	}
	
	if( row == 3 && sign == 1 ) {
		cache[ ind ] = 1 ; 
		return true ;
	} 
	cache[ ind ] = 2 ; 
	return false ; 
}

string validate( string &fin ) {
	
	memset( cache , -1 , sizeof( cache ) ) ; 
 
	//pair<int,int> trd ; 
	
	for( int i = 0 ; i < fin.size() ; i ++ ) {
		//cerr << i << endl ; 
		
		if( ok1( i , fin ) ) {
//			cerr << "h1" << endl ;
			for( int j = i + 1 ; j < fin.size() ; j ++ ) {
				bool isF = false ; 
				if( j == ( i + 1 ) ) {
					isF = true ; 
				}
				
				else isF = false ; 
				
				if( ok2( i + 1 , j , fin , isF) ) {
//					cerr << "h2" << endl ; 
					if( ok3( j + 1 , fin ) ) {
//						cout << i << " " << j << " " << endl ; 
						return "YES" ; 
					}
				}
			}
		}
		
		if( i == 2 ) {
	//		cout << fst.first << " " << fst.second << endl ; 
		}
	}
	
	return "NO" ; 
}

string solve( int L , int X , string line ) {
	string fin = "" ; 
	
	for( int i = 0 ; i < X ; i ++ ) {
		fin += line ; 
	}
	
	string res = validate( fin ) ; 
	
	return res ; 
}

int main() {
	
	int T ; 
	
	cin >> T ; 
	
	for( int i = 0 ; i < T ; i ++ ) {
		int L , X ; 
		cin >> L >> X ; 
//		scanf("%d %d",&L,&X);
		string line = "" ; 
		cin >> line ; 
		
		string res = solve( L , X , line ) ; 
		cout << "Case #" << i + 1 << ": " << res << endl ; 
	}
	return 0 ; 
}
