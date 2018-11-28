#include <bits/stdc++.h>

using namespace std;

map< int, string > mp;
map< int, int > res;
string s;
void init(){
    mp[1] = "ONE";
    mp[0] = "ZERO";
    mp[2] = "TWO";
    mp[3] = "THREE";
    mp[4] = "FOUR";
    mp[5] = "FIVE";
    mp[6] = "SIX";
    mp[7] = "SEVEN";
    mp[8] = "EIGHT";
    mp[9] = "NINE";

    return;
}

void del_string( int i ) {

    string d = mp[i];
    for( int i = 0; i < d.size(); i++ ){
	int x = s.find( d.substr( i, 1 ) );
	s[x] = '*';
    }
    //  cout << s << endl;
    return;
}

int main(){
    int t;
    cin >> t;
    int cs = 1;
    init();
    while( t-- ) {
	
	cin >> s;
	int n = s.size();
//	cout << s << endl;
	while( s.find( "Z" ) < n ){
	    del_string( 0 );
	    if ( res.count( 0 ) )
		res[0]++;
	    else res[0] = 1;
	}
	while( s.find( "U" ) < n  ){
	    del_string( 4 );
	    if( res.count( 4 ) ) res[4]++;
	    else res[4] = 1;
	}
	while( s.find( "F" ) < n){
	    del_string( 5 );
	    if( res.count( 5 ) ) res[5]++;
	    else res[5] = 1;
	}
	while( s.find( "W" ) < n){
	    del_string( 2  );
	    if( res.count( 2 ) ) res[2]++;
	    else res[2] = 1;
	}
	while( s.find( "R" ) < n){
	    del_string( 3 );
	    if( res.count( 3 ) ) res[3]++;
	    else res[3] = 1;
	}
	while( s.find( "O" ) < n){
	    del_string( 1 );
	    if( res.count( 1 ) ) res[1]++;
	    else res[1] = 1;
	}
	while( s.find( "V" ) < n){
	    del_string( 7 );
	    if( res.count( 7 ) ) res[7]++;
	    else res[7] = 1;
	}
	while( s.find( "G" ) < n ){
	    del_string( 8 );

	    if( res.count( 8 ) ) res[8]++;
	    else res[8] = 1;
	}
	while( s.find( "X" ) < n){
	    del_string( 6 );
	    if( res.count( 6 ) ) res[6]++;
	    else res[6] = 1;
	}
	while( s.find( "N" ) < n){
	    del_string( 9 );
	    if( res.count( 9 ) ) res[9]++;
	    else res[9] = 1;
	}

	cout << "CASE #" << cs << ": ";
	for( auto x: res ) {
	    int cnt = x.second;

	    while( cnt > 0 ){
		cout << x.first;
		cnt--;
	    }
	}
	cout << endl;
	res.clear();
	cs++;
    }
}
	
	
	
	
	
	
	
		
    
