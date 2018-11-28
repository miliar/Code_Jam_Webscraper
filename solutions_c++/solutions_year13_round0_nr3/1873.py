#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <list>
#include <set>
#include <iostream>
#include <sstream>

using namespace std;

bool isPal( long long num ) 
{
	ostringstream os;
	os << num;
	string s = os.str();
	int n = s.size();
	for( int i = 0; i < n  / 2; i++ ) {
		if( s[i] != s[s.size() - 1 - i] ) {
			return false;
		}
	}
	return true;
}

int main()
{
	freopen( "data.in", "r", stdin );
	freopen( "data.out", "w", stdout );
	
	vector<long long> ans;
	long long maxN = 100000000000000LL;
	for( int i = 1; i < 3000000; i++ ) {
		long long square = 1LL * i * i;
		if( square > maxN ) {
			break;
		}
		if( isPal( i ) && isPal( square ) ) {
			ans.push_back( square );
			cerr << i << ' ' << square << endl;
		}
	}

	int t;
	cin >> t;
	for(  int k = 0; k < t; k++ ) {
		long double A, B;
		cin >> A >> B;
		int res = 0;
		for( int i = 0; i < ans.size(); i++ ) {
			if( ans[i] >= A && ans[i] <= B ) {
				res++;
			}
		}
		
		
		printf( "Case #%d: %d\n", k + 1, res );
	}



	return 0;
}