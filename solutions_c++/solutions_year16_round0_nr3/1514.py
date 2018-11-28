#include <bits/stdc++.h>

using namespace std ; 

int isPrime[ 200020 ] ; 
vector<int> cur_result ; 

void getPrime() {
	for( int i = 0 ; i <= 200000 ; i ++ ) {
		isPrime[ i ] = 1 ; 
	}
	
	isPrime[ 0 ] = isPrime[ 1 ] = 0 ; 
	
	for( long long i = 2 ; i <= 200000 ; i ++ ) {
		if( isPrime[ i ] ) {
			for( long long j = i * i ; j <= 200000 ; j += i ) {
				isPrime[ j ] = 0 ; 
			}	
		}
	}
}

vector<int> bin_conv( long long x ) {
	vector<int> ret ; 
	
	while( x != 0 ) {
		int dig = x % 2 ; 
		x /= 2 ; 
		ret.push_back( dig ) ; 
	}
	
//	reverse( ret.begin() , ret.end() ) ; 
	return ret ; 
}

bool check_base( vector<int> & b , long long base ) {
	for( int i = 2 ; i < 200000 ; i ++ ) {
		if( isPrime[ i ] == 1 ) {
			long long cur_prime = i ; 
			long long cur = 1 ; 
			long long num = 0 ; 
			
			for( int j = 0 ; j < b.size() ; j ++ ) {
				num += ( b[ j ] * cur ) ; 
				num %= cur_prime ; 
				cur *= base ; 
				cur %= cur_prime ; 
			}
			
			if( num == 0 ) { 
				cur_result.push_back( cur_prime ) ;
				return true ; 
			} 
		}
	}
	
	return false ; 
}

bool ok( long long curNum ) {

	vector<int> b = bin_conv( curNum ) ; 
	
	int cnt = 0 ; 
	
	cur_result.clear() ; 
	
	for( int i = 2 ; i <= 10 ; i ++ ) {
		if( check_base( b , i ) ) cnt ++ ; 
	}
	
	if( cnt == 9 ) {
		reverse( b.begin() , b.end() ) ;
		
		for( int i = 0 ; i < b.size() ; i ++ ) {
			cout << b[ i ] ;
		}
		
		for( int i = 0 ; i < cur_result.size() ; i ++ ) {
			cout << " " << cur_result[ i ] ; 
		}
		cout << endl ; 
		return true ; 
	}
	return false ; 
}

int main() {

	getPrime() ; 
	
	int T ;
	int N , J ; 
	
	cin >> T ; 
	cin >> N >> J ; 
	int cnt = 0 ; 
	
	cout << "Case #1:"<<endl ;
	for( long long i = ( 1LL << 32LL ) - 1 ; cnt < J ; i -= 2 ) {
		if( ok( i ) ) cnt ++ ; 	
	} 
	
	return 0 ; 
}
