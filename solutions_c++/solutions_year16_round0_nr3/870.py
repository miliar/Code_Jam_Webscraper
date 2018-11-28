#include <bits/stdc++.h>

using namespace std;

map< string, int > found;

int primes[ 100000000 ], p[100000000], pcnt;

void setp( ) {
    primes[0] = 1;
    primes[1] = 1;
    
    for( int i = 2; i <= 15000; i++){
	if( !primes[i] ){
	    p[pcnt] = i;
	    pcnt++;
	    for( int j = i + i; j < 100000000; j += i ){
		primes[j] = 1;
	    }
	}
    }
    return;
}

int check_prime( long long n ) {
    int sq = sqrt( n )+1;
    int found = 0;
    int i = 0;
    int sol = 0;
    for( i = 0; i < pcnt && p[i] < sq; i++){
	if( n % p[i] == 0 ){
	    found = 1;
	    sol = p[i];
	    break;
	}
    }
    if( !found && ( i == pcnt )){
	for( long long j = p[pcnt-1] + 1; j <= sq; j++ )
	    if( n % j == 0 ){
		found = 1;
		sol = j;
		break;
	    }
    }
    return sol;
}

//char out[100];
string bstring( long long n ){
    long long x = 2;
    string s = "";
    while( n ){
	int x = n % 2;
	s = to_string( x ) + s;
	n/=2;
    }
    return s;
}

long long conv_base( string s, long long k ){
    long long num = 0;
    for( int i = 0; i < s.length(); i++ )
	num = num*k + ( s[i] - '0' );
    return num;
}

int brute( int n, int req ){
    long long num = 1;
    for(int j = 1; j < n; j++ ) num*=2;
    num += 1;
    int cnt = 0;
    
    while( cnt < req ){
	string s = bstring( num );
	int valid = 1;
	int div[11];
	for( int base = 2; base <= 10; base++ ){
	    long long n = conv_base( s, base );
//	    cout << n << " " << base << endl;
	    div[base] = check_prime( n );
	    if( !div[base] ){
		valid = 0;
		break;
	    }
	}
	if( valid ){
	    cout << s;
	    for( int base = 2; base <= 10; base++ )
		cout << " " << div[ base ] ;
	    cout << endl;
	    req--;
	}
	num+= 2;
    }
}

	    
	
int main( ){
    int t;
    setp();
    cin >> t;
    for( int j = 0; j < t; j++ ){
	cout << "Case #1:" << endl;
	int n, req;
	cin >> n >> req;
	brute( n, req );
    }
    return 0;
}
    
    

	
