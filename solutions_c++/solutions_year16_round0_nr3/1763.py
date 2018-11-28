#include <fstream>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <math.h>
#include <bitset>
using namespace std;

void solve();

typedef unsigned long long int ll;

ifstream ifs( "data.txt" );
ofstream ofs("result.txt");

int main( void ) {


	int T;
	ifs >> T;
	for( int i = 0; i < T; i++ ) {
		ofs << "Case #" << i+1 << ":";
		solve();
	}

	return 0;
}


void solve() {

	ll N, J;

	ofs << endl;

	ifs >> N >> J;

	ll jamcnt = 0;
	ll lim = (1LL<<(N-2LL));

	vector<int> p((1<<15),0);
	vector<ll> v;
	p[1] = true;
	p[0] = true;
	for( ll i = 2; i < p.size(); i++ ) {
		if( p[i] ) continue;
		for( ll j = 2*i; j < p.size(); j+=i ) {
			p[j] = true;
		}
	}

	for( ll i = 2; i < p.size(); i++ ) {
	
		if( !p[i] ) {
			v.push_back(i);
		}

	}


	for( ll i = 0; i < lim && jamcnt < J; i++ ) {

		bitset<33> b(i);

		b <<= 1;
		b[N-1] = 1;
		b[0] = 1;

		vector< ll > d;
		
		if( b[0] == false || b[N-1] == false ){ continue; }
		

		
		for( ll j = 2; j <= 10; j++ ) {
			
			for( ll l = 0; l < v.size(); l++ ) {
				ll cnt = 0;
				for( ll k = 0; k < N; k++ ) {
					cnt *= j;
					if( b[N-k-1] ) {
						cnt ++;
					}
					cnt %= v[l];
				}

				if( cnt % v[l] == 0 ) {
					d.push_back( v[l] );
					break;
				}
			}
			
			
		}
		

		if( d.size() == 9 ) {
			for( ll i = 0; i < N; i++ )
				ofs << b[N-1-i];
			for( ll i = 0; i < (ll)d.size(); i++ )
				ofs << " " << d[i];
			ofs << endl;
			jamcnt ++;
		}

	}


}