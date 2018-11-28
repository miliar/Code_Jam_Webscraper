#include <cstdio>
#include <algorithm>
#include <queue>
#include <iostream>
#include <map>
#include <set>
#include <cmath>
#include <string>
#include <cstring>
#include <list>
using namespace std ;
const int lim = 1000006 ;

int N ;
long long arr[lim], K ;

void caso() {
	long long res = 0LL ;

	cin >> K >> N ;
	for( int i=0; i<N; i++ ) 
		cin >> arr[i] ;

	sort( arr, arr+N ) ;

	for( int i=0; i<N; i++ ) {
		if( K>arr[i] ) {
			K += arr[i] ;
			continue ;
		}
		long long tmp = K, t=0LL ;
		if( tmp>1 ) {
			while( tmp<=arr[i] ) {
				tmp += tmp-1 ;
				t ++ ;
			}
		}
		else {
			t = (1LL<<50) ;
			res += N-i ;
			break ;
		}
		if( t>=N-i ) {
			res += N-i ;
			break ;
		}
		K = tmp ;
		res += t ;
		K += arr[i] ;
	}

	cout << res << endl ;

}

int main() {
	int T ;

	cin >> T ;

	for( int i=0; i<T; i++ ) {
		cout << "Case #" << i+1 << ": " ;
		caso() ;
	}

	return 0 ;
}


