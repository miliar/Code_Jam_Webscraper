/*
	// Author: Suraj Bora
	// Email: surajbora021@gmail.com

*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <locale>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

// some typedefs

typedef unsigned long long int ulli;
typedef long long int lli;
typedef long long ll;
typedef pair < int, int > pii;
typedef vector< int > vi;
typedef vector< lli > vlli;
typedef vector< char > vc ;
typedef vector< pii > vpii;
typedef set< int > si;
typedef vector< string > vs;
typedef priority_queue< int > pq;
typedef priority_queue<int, std::vector<int>, std::greater<int> > mpq;

// some macros

#define PINF INT_MAX
#define NINF INT_MIN

#define FOR( i, a, b )    for( int i= a; i<=(b); ++i )
#define rep( i, n ) 	  for( int i= 0; i< (n); ++i )
#define fori( i, x)       for( typeof(x.begin()) i=x.begin(); i!=x.end(); ++i )


#define f 			      first
#define s 	              second
#define pb                push_back
#define mp 		          make_pair
#define sz(x)       	  (int)( x.size() )
#define in 				  insert
#define init( x, v )	  memset( x, v, sizeof x )




int main(){

	int T;
	int smax;
	string s;

	freopen( "inputLA.in", "r", stdin );
	freopen( "outputLA.txt", "w", stdout );

	scanf("%d", &T );

	FOR( t, 1, T ){

		cin >> smax >> s;

		int count= 0;

		int till_sum= s[0]-'0';		// people stood up without paid

		for( int i=1; i< s.length(); ++i ){

			if( till_sum < i ){	// less people are standing up than required to stand audience of happiness i

				count+= i-till_sum;

				till_sum+= i - till_sum + s[i]- '0';

			}else if( till_sum== i ){

				till_sum+= s[i]-'0';
			}else{

				till_sum+= s[i]-'0';
			}
		}

		if( till_sum >= smax )
		printf("Case #%d: %d\n", t, count );
	}

}