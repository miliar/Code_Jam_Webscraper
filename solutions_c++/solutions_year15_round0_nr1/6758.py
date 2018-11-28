#include <iostream>
#include <sstream>
#include <bitset>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <numeric>
#include <list>
#define FOR(i,A) for(typeof (A).begin() i = (A).begin() ; i != (A).end() ; i++)
#define mp make_pair
#define debug( x ) cout << #x << " = " << x << endl
#define clr(v,x) memset( v, x , sizeof v )
#define all(x) (x).begin() , (x).end()
#define rall(x) (x).rbegin() , (x).rend()
#define f(i,a,b) for(int i = a ; i < b ; i++)
#define fd(i,a,b) for(int i = a ; i >= b ; i--)
#define PI acos( -1.0 )
#define EPS 1E-9
#define TAM 1010

using namespace std;

typedef pair<int,int> ii ;
typedef long long ll ;
typedef long double ld ;
typedef pair<int,ii> pii ;

int main(){

	int test , n ;
	char s[ TAM ] ;
	scanf("%d" , &test ) ;
	f( k , 1 , test+1 ){
		scanf("%d%s" , &n , s ) ;
		int current = s[ 0 ] - '0' , resp = 0 ;
		f( shy , 1 , n+1 ){
			int lvl = s[ shy ] - '0' ;
			if( shy > current ){
				resp += shy - current ;
				current += shy - current ;
			}
			current += lvl ;
		}
		printf("Case #%d: %d\n" , k , resp ) ;
	}
	return 0 ;
}

