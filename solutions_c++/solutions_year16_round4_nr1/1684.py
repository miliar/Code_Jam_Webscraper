#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<list>

using namespace std;

string A[ 3 ] = {"PR","PS","RS"};

string recur( int n, int p, int r, int s ){
	if( n == 1 ){
		if( p == 1 && r == 1 && s == 0 )
			return "PR";
		if( p == 1 && r == 0 && s == 1 )
			return "PS";
		if( p == 0 && r == 1 && s == 1 )
			return "RS";
		return "IMPOSSIBLE";
	}
	if( n == 2 ){
		if( p == 2 && r == 1 && s == 1 )
			return "PRPS";
		if( p == 1 && r == 2 && s == 1 )
			return "PRRS";
		if( p == 1 && r == 1 && s == 2 )
			return "PSRS";
		return "IMPOSSIBLE";
	}
	if( n == 3 ){
		if( p == 2 && r == 3 && s == 3 )
			return "PRRSPSRS";
		if( p == 3 && r == 2 && s == 3 )
			return "PRPSPSRS";
		if( p == 3 && r == 3 && s == 2 )
			return "PRPSPRRS";
		return "IMPOSSIBLE";			
	}
	if( p&1 || r&1 || s&1 )
		return "IMPOSSIBLE";
	string res = recur( n-1 , p/2, r/2, s/2 );
	if( res[ 0 ] == 'I' )
		return "IMPOSSIBLE";
	return res+res;
}

int main(){
	int kases; cin >> kases;
	for( int kase = 1; kase <= kases; kase++ ){
		int N; cin >> N;
		int P, R, S; cin >> R >> P >> S;
		list< int > c;
		string res = recur( N, P, R, S);
		cout << "Case #"<<kase<<": " << res << endl;
	}
}
