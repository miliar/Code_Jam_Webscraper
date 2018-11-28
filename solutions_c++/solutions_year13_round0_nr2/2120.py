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

int main(){
	freopen("A-large-practice2.in.txt","rt",stdin) ;
	freopen("A-large-practice2.out.txt","wt",stdout) ;

	int T , l=1 , N , M , arr[100][100] ;
	cin >> T ;
	while( T-- ){
		cin >> N >> M ;
		for( int i=0 ; i<N ; i++ ){
			for( int j=0 ; j<M ; j++ )	cin >> arr[i][j] ;
		}
		
		int check ;
		bool p1 , p2 ;
		for( int i=0 ; i<N ; i++ ){
			for( int k=0 ; k<M ; k++ ){
				p1=true ;	p2=true ;
				//--------------------------------------------------------------
				check=arr[i][k] ;
				for( int j=0 ; j<M ; j++ ){		if( check<arr[i][j] ){	p1=false ;	break ;	}		}
				for( int j=0 ; j<N ; j++ ){		if( check<arr[j][k] ){	p2=false ;	break ;	}		}
				//--------------------------------------------------------------
				if( !p1 && !p2 )	break ;
			}
			if( !p1 && !p2 )	break ;
		}
		if( !p1 && !p2 )	cout << "Case #" << l << ": NO" << endl ;
		else				cout << "Case #" << l << ": YES" << endl ;
		l++ ;
	}
	//--------------------------------------------------------------------------
	//freopen("A-small-practice2.in.txt","rt",stdin) ;
	//freopen("A-small-practice2.out.txt","wt",stdout) ;
	//--------------------------------------------------------------------------
	return 0 ;
}
