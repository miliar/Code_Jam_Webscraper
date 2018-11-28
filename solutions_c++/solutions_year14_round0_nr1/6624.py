#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <utility> 
#include <stack>
#include <cstring> 
#include <cmath>
#include <stdio.h>
#include <string.h>

#define sz(v) ((int)v.size())
#define rep(i,m) for(int i=0;i<(int)(m);i++)
 
#define oo ((int) 1e9)
#define mp make_pair

using namespace std;
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("out.in","w",stdout);
	int t , a , b  , x , c , ca=1 ;  
	vector<int > a1 ; 
	vector<int > b1 ;

	cin >> t ; 
	while ( t-- ) {

		cin >> a ; 
		c = 0 ;
		a1.clear() ; 
		b1.clear() ; 

		rep ( i , 4 ) 
			rep(j , 4 ) {
				cin >> x ;
				if ( i+1 == a ) 
					a1.push_back(x) ; 
		}

		cin >> b ; 

		rep ( i , 4 ) 
			rep(j , 4 ) {
				cin >> x ;
				if ( i+1 == b ) 
					b1.push_back(x) ; 
		}
		

		rep( i , 4 ) 
			rep ( j , 4 ) 
			if ( a1[i] == b1[j] ) {
				c++ ;
				x = a1[i] ; 
			}


		if ( c == 0 ) 
			cout << "Case #"<<ca++<<": Volunteer cheated!" << endl;
		else if ( c == 1 ) 
			cout << "Case #"<<ca++<<": "<<x << endl;
		else
			cout << "Case #"<<ca++<<": Bad magician!" << endl;

	}
	return 0;
}