#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
int mod = 1000000007;

ifstream fin( "D1.in" );
ofstream fout( "D1.out" );
#define cin fin
#define cout fout

#define MAX 10000
struct Trie{
	int next[27];
};

Trie T[MAX];
int tot = 1;

void insert( string s ){
	int cur = 0;
	for( int i = 0; i < s.length(); i++ ){
		int idx = s[i] - 'A';
		if( T[cur].next[idx] == -1 ){
			T[cur].next[idx] = tot;
			cur = tot++;
		}
		else cur = T[cur].next[idx];
	}
}

int count( vector<string> v ){
	tot = 1;
	for( int i = 0; i < MAX; i++ )
		memset( T[i].next, -1, sizeof T[i].next );
	for( int i = 0; i < v.size(); i++ ){
		insert( v[i] );
	}
	return tot;
}

int test, m, n;
string all[100];
int pre[( 1 << 20 )];
int dp1[( 1 << 15 )][10];
long long dp2[( 1 << 15 )][10];

int solveMax( int mask, int rem ){
	int& ref = dp1[mask][rem];
	if( ref != -1 )
		return ref;
	if( rem == 0 ){
		if( mask == 0 )
			return ref = 0;
		else return ref = -1000000;
	}
	ref = -1000000;
	for( int ms = 1; ms < ( 1 << m ); ms++ )
		if( ( ms & mask ) == ms )
			ref = max( ref, pre[ms] + solveMax( mask - ms, rem - 1 ) );
	return ref;
}

long long solveAll( int mask, int rem ){
	//cout << mask << ' ' << rem << endl;
	long long& ref = dp2[mask][rem];
	if( ref != -1 )
		return ref;
	if( rem == 0 ){
		if( mask == 0 )
			return ref = 1;
		return ref = 0;
	}
	ref = 0;
	for( int ms = 1; ms < ( 1 << m ); ms++ )
		if( ( ms & mask ) == ms  && dp1[mask][rem] == pre[ms] + dp1[mask - ms][rem - 1] ){
			ref += solveAll( mask - ms, rem - 1 );
			ref %= mod;
			//if( rem == 2 )
			//	cout << "GGG " << ms << ' ' << mask << ' ' << solveAll( mask - ms, rem - 1 ) << endl;
		}
	return ref;
}

int main()
{
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		memset( dp1, -1, sizeof dp1 );
		memset( dp2, -1, sizeof dp2 );
		cin >> m >> n;
		for( int i = 0; i < m; i++ )
			cin >> all[i];
		for( int i = 1; i < ( 1 << m ); i++ ){
			vector< string > v;
			for( int j = 0; j < m; j++ )
				if( i & ( 1 << j ) )
					v.push_back( all[j] );
			//cout << i << ' ' << count( v ) << endl;
			pre[i] = count( v );
		}
		int mx = solveMax( ( 1 << m ) - 1, n );
		long long cnt = solveAll( ( 1 << m ) - 1, n );
		cout << "Case #" << T << ": " << mx << ' ' << cnt << endl;
		//cout << mx << endl;
	}
	return 0;
}