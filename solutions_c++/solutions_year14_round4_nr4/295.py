#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <cassert>
#include <cmath>
#include <deque>
#include <map>
#include <cstring>
#include <set>

using namespace std;

typedef pair<int,int> P;
typedef long long LL;

string s[8];
int server[8]; // server assign to a given string
int m; // number of strings
int n; // number of servers

int bucket[4];
LL server_cost[1<<8];
LL max_cost;
LL max_cost_cnt;
const LL MOD = 1000000007;

void calc_server_cost() {
	for( int i = (1<<m)-1; i >= 0; --i ) {
		set<string> prefixes;
		for( int j = 0; j < m; ++j ) {
			if( i & (1<<j) ) {
				for( int len = 1; len <= (int)s[j].size(); ++len ) {
					prefixes.insert( s[j].substr(0,len) );
				}
			}
		}
		server_cost[i] = prefixes.size()+1;
	}
}

void assign( int k ) {
	if( k == m ) {
		int server_mask = 0;
		for( int i = 0; i < m; ++i ) {
			server_mask |= 1<<server[i];
		}
		if( server_mask != (1<<n)-1 ) return;

		for( int i = 0; i < n; ++i ) bucket[i] = 0;
		for( int i = 0; i < m; ++i ) {
			bucket[server[i]] |= 1<<i;
		}
		LL cost = 0;
		for( int i = 0; i < n; ++i ) {
			cost += server_cost[bucket[i]];
		}
		if( cost > max_cost ) {
			max_cost = cost;
			max_cost_cnt = 1;
		} else if( cost == max_cost ) {
			max_cost_cnt = (max_cost_cnt+1)%MOD;
		}
		return;
	}

	for( int i = 0; i < n; ++i ) {
		server[k] = i;
		assign( k+1 );
	}
}

int main() {
	int cases;
	cin >> cases;

	for( int caseid = 1; caseid <= cases; ++caseid ) {
		cout << "Case #" << caseid << ": ";

		cin >> m >> n;
		assert( m <= 8 );
		for( int i = 0; i < m; ++i ) {
			cin >> s[i];
		}
		calc_server_cost();
		max_cost = -1;
		assign(0);
		cout << max_cost << ' ' << max_cost_cnt << endl;
	}
	return 0;
}

