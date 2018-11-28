#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define all(x) x.begin(),x.end() 
#define MAXN 
using namespace std;
typedef pair < int , int > pii;
typedef pair < pii , int > pii3;
int read(){ int res(0),sign(1); char c;
	while(1){ c = getchar(); if('0' <= c && c <= '9') { res = c - '0'; break; } else if(c == '-') { sign = -1; break; } }
	while(1){ c = getchar(); if('0' <= c && c <= '9') res = res*10 + c - '0'; else break; }
	return res * sign;
}

int N,a,b,c;

string rec( char x , int s ) {

	if( s == N ) return ( x == 'R' ) ? "R" : (x == 'S') ? "S" : "P";

	if( x == 'S' ) {
		string str1 = rec('P',s+1);
		string str2 = rec('S',s+1);

		if( (str1 + str2) < (str2 + str1) )
			return str1 + str2;
		else
			return str2 + str1;

	} else if( x == 'P' ) {
		string str1 = rec('P',s+1);
		string str2 = rec('R',s+1);

		if( (str1 + str2) < (str2 + str1) )
			return str1 + str2;
		else
			return str2 + str1;
	} else {
		string str1 = rec('R',s+1);
		string str2 = rec('S',s+1);

		if( (str1 + str2) < (str2 + str1) )
			return str1 + str2;
		else
			return str2 + str1;
	}


}

pii3 p(int n);
pii3 s(int n);

pii3 r(int n) {

	if( !n ) return make_pair( make_pair(1 , 0) , 0 );
	pii3 t1 = r(n-1);
	pii3 t2 = s(n-1);
	return make_pair( make_pair( t1.f.f + t2.f.f , t1.f.s + t2.f.s ) , t1.s + t2.s );
}

pii3 p(int n) {

	if( !n ) return make_pair( make_pair(0 , 1) , 0 );
	pii3 t1 = p(n-1);
	pii3 t2 = r(n-1);
	return make_pair( make_pair( t1.f.f + t2.f.f , t1.f.s + t2.f.s ) , t1.s + t2.s );
}

pii3 s(int n) {

	if( !n ) return make_pair( make_pair(0 , 0) , 1 );
	pii3 t1 = s(n-1);
	pii3 t2 = p(n-1);

	return make_pair( make_pair( t1.f.f + t2.f.f , t1.f.s + t2.f.s ) , t1.s + t2.s );
}

vector < string > res;

void solve() {

	N = read(); a = read(); b = read(); c = read();

	pii3 t = make_pair( make_pair( a , b ) , c );

	if( r(N) == t )
		res.push_back( rec('R',0) );
	if( p(N) == t )
		res.push_back( rec('P',0) );
	if( s(N) == t )
		res.push_back( rec('S',0) );

	sort( all(res) );

	if( res.empty() )
		printf("IMPOSSIBLE\n");
	else
		cout << res[0] << endl;

	res.clear();

}
int main()
{
	freopen( "input.txt" , "r" , stdin );
	freopen( "output.txt" , "w" , stdout );
	int T = read() , i;
	FOR(i,1,T) {
		printf("Case #%d: " , i );
		solve();
	}
	return 0;
}
