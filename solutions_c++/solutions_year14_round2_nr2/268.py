#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#define P pair< char, int >
using namespace std;

ifstream fin( "B2.in" );
ofstream fout( "B2.out" );
#define cin fin
#define cout fout

long long dp[70][2][2][2];
long long a, b, k;

int newCmp( int idx, int bit, int preCmp, long long num ){
	if( preCmp == 0 )
		return 0;
	if( bit == 1 )
		return 1;
	if( bit == 0 && ( num & ( 1LL << idx ) ) > 0 )
		return 0;
	return 1;
}

long long solve( int idx, int cmpA, int cmpB, int cmpK ){
	//cout << idx << ' ' << cmpA << ' ' << cmpB << ' ' << cmpK << endl;
	if( idx == -1 ){
		
		if( cmpA == cmpB && cmpB == cmpK && cmpK == 0 ){
			
			return 1;
		}
		return 0;
	}
	
	long long& ref = dp[idx][cmpA][cmpB][cmpK];
	if( ref != -1 )
		return ref;
	
	ref = 0;
	for( int i = 0; i < 2; i++ ){
		if( cmpA == 1 && i == 1 && ( a & ( 1LL << idx ) ) == 0 )
			continue;
		for( int j = 0; j < 2; j++ ){
			if( cmpB == 1 && j == 1 && ( b & ( 1LL << idx ) ) == 0 )
				continue;
			int bAnd = ( i & j );
			if( cmpK == 1 && bAnd == 1 && ( k & ( 1LL << idx ) ) == 0 )
				continue;
			/*cout << "GGF " << i << ' ' << j << endl;
			cout << idx << ' ' << i << ' ' << cmpA << ' ' << a << endl;
			cout << newCmp( idx, i, cmpA, a ) << endl;
			*/
			ref += solve( idx - 1, newCmp( idx, i, cmpA, a ), newCmp( idx, j, cmpB, b ), newCmp( idx, bAnd, cmpK, k ) );
			//cout << i << ' ' << j << ' ' << ref << endl;
		}
	}
	return ref;
}


int main()
{
	//cout << newCmp( 0, 0, 1, 1 ) << endl;
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		cin >> a >> b >> k;
		memset( dp, -1, sizeof dp );
		long long cnt = solve( 50, 1, 1, 1 );
		cout << "Case #" << T << ": " << cnt << endl;
	}

	return 0;
}