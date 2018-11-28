#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

bool check( const vector<int>& v )
{
	for ( size_t j = 0; j < v.size(); j++ ) {
		int sum = 0;
		for ( size_t k = 0; k <= j; k++ ) {
			sum += v[k] * v[j-k];
		}
		if ( sum > 9 ) {
			return false;
		}
	}
	return true;
}

struct BigInt {
	BigInt( const vector<int>& _v ) : v(_v) {}
	BigInt( const string& s ) {
		for ( auto c : s ) {
			v.push_back(c-'0');
		}
	}
	bool operator<( const BigInt& rhs ) const {
		if ( v.size() != rhs.v.size() ) {
			return v.size() < rhs.v.size();
		}
		return v < rhs.v;
	}
	vector<int> v;
};

int main()
{
	vector<vector<int> > DP;
	DP.push_back( vector<int>(1,1) );
	DP.push_back( vector<int>(1,2) );
	DP.push_back( vector<int>(1,3) );
	DP.push_back( vector<int>(2,1) );
	DP.push_back( vector<int>(2,2) );
	set<vector<int> > all(DP.begin(),DP.end());
	while ( !DP.empty() ) {
		set<vector<int> > DP2;
		for ( int x = 0; x < DP.size(); x++ ) {
			for ( int a = 0; a < 3; a++ ) {
				vector<int> v = DP[x];
				v.push_back(a);
				v.insert(v.end(), DP[x].rbegin(), DP[x].rend());
				if ( check(v) ) {
					if ( all.insert(v).second ) {
						v = DP[x];
						v.push_back(a);
						DP2.insert(v);
					}
				}

				v = DP[x];
				v.push_back(a);
				v.push_back(a);
				v.insert(v.end(), DP[x].rbegin(), DP[x].rend());
				if ( check(v) ) {
					if ( all.insert(v).second ) {
						v = DP[x];
						v.push_back(a);
						DP2.insert(v);
					}
				}
			}
		}
		DP.clear();
		for ( auto e : DP2 ) {
			if ( e.size() < 30 ) {
				DP.push_back(e);
			}
		}
	}

	vector<BigInt> v;
	for ( auto e : all ) {
		vector<int> p2(e.size()*2-1);
		for ( size_t i = 0; i < e.size(); i++ ) {
			for ( size_t j = 0; j < e.size(); j++ ) {
				p2[i+j] += e[i] * e[j];
			}
		}
		v.push_back( p2 );
	}
	sort( v.begin(), v.end() );

	int T;
	cin >> T;
	for ( int t = 1; t <= T; t++ ) {
		string A, B;
		cin >> A >> B;
		printf( "Case #%d: %d\n", t, upper_bound(v.begin(),v.end(),BigInt(B)) - lower_bound(v.begin(),v.end(),BigInt(A)) );
	}
	return 0;
}
