#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

const long long mod = 1000002013LL;

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	int t;
	cin >> t;
	for( int tt = 1; tt <= t; tt++ ) {
		vector<pair<int, int> > stackIn;
		vector<pair<int, int> > stackOut;
		long long mustPay = 0;


		int n, m;
		cin >> n >> m;
		for( int i = 0; i < m; i++ ) {
			int s, e, count;
			cin >> s >> e >> count;
			
			int len = e - s;
			long long res = ( 2LL * n - len - 1 ) * (len) / 2;
			if( len == 0 ) {
				res = 0;
			}
			res %= mod;
			res *= count;
			res %= mod;
			mustPay += res;
			mustPay %= mod;
			stackIn.push_back( make_pair( s, count ) );
			stackOut.push_back( make_pair( e, count ) );
		}
		
		sort( stackIn.begin(), stackIn.end() );
		sort( stackOut.begin(), stackOut.end() );

		int starti = 0, endi = 0;
		long long actualPay = 0;

		while( true ) {
			if( starti < stackIn.size() - 1 && stackIn[starti].first <= stackOut[endi].first ) {
				starti++;
				continue;
			}
			int curI = starti;
			while( stackIn[curI].first > stackOut[endi].first ) {
				curI--;
			}
			int count = stackOut[endi].second;
			int pos = stackOut[endi].first;
			while( count > 0 ) {
				int minCount = min( count, stackIn[curI].second );
				int len = pos - stackIn[curI].first;
				long long res = (2LL * n - len - 1 ) * ( len) / 2;
			//	cerr << "Test: " << stackIn[curI].first << " " << pos << endl;
				if( len == 0 ) {
					res = 0;
				}
				//cerr << res << endl;
				res %= mod;
				res *= minCount;
				res %= mod;
				actualPay += res;
				actualPay %= mod;
				count -= minCount;
				stackIn[curI].second -= minCount;
				curI--;
			}

			endi++;
			if( endi >= stackOut.size() ) {
				break;
			}

		}

		printf( "Case #%d: ", tt );
		
		//cerr << mustPay	<< endl;
		//cerr << actualPay << endl;
		long long ans = mustPay + mod - actualPay;
		ans %= mod;
		cout << ans;
	
		cout << endl;
	}
	return 0;
}

