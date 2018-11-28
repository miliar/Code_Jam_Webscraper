#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std ;

vector<long long> nums ; 

bool isPalin( long long X ) {
	ostringstream oss ;
	
	oss << X ;
	
	string a = oss.str() ;
	string b = a ;
	reverse( b.begin() , b.end() ) ;
	
	return a == b ; 
}

void gen() {
	for( long long i = 1 ; ; i ++ ) {
	
		long long sq = i * i ;
		
		if( sq > 100000000000000LL ) break ; 
			
		if( isPalin( i ) && isPalin( sq ) ) {
			nums.push_back( sq ) ; 
		}
	}	
}

int res( long long A , long long B ) {
	int en = upper_bound( nums.begin() , nums.end() , B ) - nums.begin() ;
	int st = lower_bound( nums.begin() , nums.end() , A ) - nums.begin() ;
	
	return en - st ;
}

int main() {

	int T ; 
	
	gen() ;
//	calc() ;
	
	cin >> T ;
	
	long long A , B ; 
	
	for( int i = 0 ; i < T ; i ++ ) {
		cin >> A >> B ;
		int r = res( A , B ) ;
		cout << "Case #" << i + 1 << ": " << r << '\n' ;
	}
	
	return 0 ; 
}
