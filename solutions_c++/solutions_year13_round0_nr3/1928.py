#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <stdio.h>
#include <cmath>
#include <math.h>
#include <queue>

using namespace std;

bool plaind( long long i ){
	long long j=0 , k=i ;
	while( k!=0 ){	j*=10 ;		j+=k%10 ;		k/=10 ;		}
	if( j==i )	return true ;
	return false ;
}

vector< long long > isplaind ;
void ch(){
	for( long long i=1 ; i<=2001002 ; i++ ){
		if( plaind( i ) && plaind( i*i ) )
		isplaind.push_back(i*i) ;
	}
}

int main(){
	freopen("A-large-practice3.in.txt","rt",stdin) ;
	freopen("A-large-practice3.out.txt","wt",stdout) ;
	ch() ;
	long long T , a , b , l=1 ;
	cin >> T ;
	while( T-- ){
		cin >> a >> b ;
		long long res=0 ;
		for( long long i=0 ; i<isplaind.size() ; i++ ){
			if( isplaind[i]>=a && isplaind[i]<=b )
			res++ ;
		}
		cout << "Case #" << l << ": " << res << endl ;
		l++ ;
	}
	//--------------------------------------------------------------------------
	//freopen("A-small-practice3.in.txt","rt",stdin) ;
	//freopen("A-small-practice3.out.txt","wt",stdout) ;
	//--------------------------------------------------------------------------
	return 0 ;
}
