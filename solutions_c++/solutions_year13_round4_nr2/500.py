#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

void tour( vector<int>& v )
{
	if ( v.size() == 1 ) return;

	vector<int> w, l;
	for ( int i = 0; i < v.size(); i+= 2 ) {
		w.push_back( min( v[i], v[i+1] ) );
		l.push_back( max( v[i], v[i+1] ) );
	}

	v.clear();
	tour( w );
	tour( l );
	v = w;
	v.insert( v.end(), l.begin(), l.end() );
}

void test(int p)
{
	vector<int> v(8);
	for ( int i = 0; i < 8; i++ ) v[i] = i;

	vector<bool> all(8,true), one(8,false);
	do {
		auto r = v;
		tour(r);
		for ( int i = 0; i < p; i++ ) {
			one[r[i]] = true;
		}
		for ( int i = p; i < 8; i++ ) {
			all[r[i]] = false;
		}
	} while( next_permutation(v.begin(),v.end()) );
	
	for ( int i = 7; i >= 0; i-- ) {
		if ( all[i] ) {
			cerr << i << " ";
			break;
		}
	}
	for ( int i = 7; i >= 0; i-- ) {
		if ( one[i] ) {
			cerr << i << endl;
			break;
		}
	}
}

__int64 a( __int64 n, __int64 p ) {
	__int64 g = 1LL<<n;
	__int64 r = 0, t = 2;
	g /= 2;
	__int64 add = g/2;
	for ( int i = 0; i < n; i++ ) {
		if ( p <= g ) return r;
		g += add;
		add /= 2;
		r += t;
		t *= 2;
	}
	return (1LL<<n)-1;
}

__int64 b( __int64 n, __int64 p ) {
	__int64 g = 0, t = 2, a = 1LL<<(n-1), r = 0;
	for ( int i = 0; i < n; i++ ) {
		if ( p-1 <= g ) return r;
		g += t;
		t *= 2;
		r += a;
		a /= 2;
	}
	return (1LL<<n)-1;
}

int main()
{
    int T;
    cin >> T;
    for ( int test = 1; test <= T; test++ ) {
		__int64 N, P;
		cin >> N >> P;
        printf( "Case #%d: %lld %lld\n", test, a(N,P), b(N,P) );
    }
    return 0;
}
