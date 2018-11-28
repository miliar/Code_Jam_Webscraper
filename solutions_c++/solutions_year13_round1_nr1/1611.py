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
	freopen("A-small-practice.in.txt","rt",stdin) ;
	freopen("A-small-practice.out.txt","wt",stdout) ;
	//--------------------------------------------------------------------------
	//--------------------------------------------------------------------------
	
	int T , l=1 , r , t , res , ind=0 ;
	long long area1 , area2 ;
	cin >> T ;
	while( T-- ){
		cin >> r >> t ;
		res=0 ;		ind=0 ;
		while( 1 ){
			area1=(r+ind+1)*(r+ind+1) ;		area2=(r+ind)*(r+ind) ;
			ind+=2 ;
			if( (area1-area2)<=t ){		res++ ;		t-=(area1-area2) ;	}
			else	break ;
		}
		cout << "Case #" << l << ": " << res << endl ;
		l++ ;
	}
	
	//--------------------------------------------------------------------------
	//--------------------------------------------------------------------------
	//freopen("A-large-practice.in.txt","rt",stdin) ;
	//freopen("A-large-practice.out.txt","wt",stdout) ;
	return 0 ;
}
