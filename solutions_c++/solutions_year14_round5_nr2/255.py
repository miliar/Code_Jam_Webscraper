#include <iostream>
#include <fstream>
#define MAXN 205
using namespace std;

int H[MAXN], G[MAXN];

int dp[MAXN][2000];
int test;
int n, p, q;

ifstream fin( "B1.in" );
ofstream fout( "B1.out" );
#define cin fin
#define cout fout

int solve( int idx, int rem ){
	if( idx == n )
		return 0;
	int& ref = dp[idx][rem];
	if( ref != -1 )
		return ref;
	//if( idx == 2 )
	//	cout << idx << "Fdfd " << rem << endl;
	ref = solve( idx + 1, rem + ( H[idx] + q - 1 ) / q );
	for( int i = 0; i <= rem; i++ ){
		if( i * p >= H[idx] ){
			ref = max( ref, G[idx] + solve( idx + 1, rem - i ) );
			break;
		}
		int vl = H[idx] - i * p;
		if( vl < q )
			continue;
		int need = 0;
		while( vl > q && ( vl % q > p || vl % q == 0 ) )
			vl -= ( p + q ), need++;
		//if( idx == 2 && rem == 1 )
		//	cout << "1 = " << vl << ' ' << i << ' ' << need << endl;
		if( vl == 0 )
			ref = max( ref, G[idx] + solve( idx + 1, rem - i ) );
		else if( vl > q )
			ref = max( ref, G[idx] + solve( idx + 1, rem + ( vl ) / q - 1 - i ) );
	}
	return ref;
}

int main()
{
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		cin >> p >> q >> n;
		for( int i = 0; i < n; i++ )
			cin >> H[i] >> G[i];
		memset( dp, -1, sizeof dp );
		cout << "Case #" << T << ": " << solve( 0, 1 ) << endl;
	}
	return 0;
}