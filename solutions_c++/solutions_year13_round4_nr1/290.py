
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <cstdio>
#include <set>
#include <map>
#include <sstream>
#include <cmath>
#include <functional>
#include <cassert>
#include <queue>
#include <cstring>
#include <limits>

using namespace std;

typedef long long LL;
typedef pair<int,int> PI;
const int dr[] = {-1,0,1,0};
const int dc[] = {0,1,0,-1};

struct trip_t {
	int from, to;
	int cnt;
};

struct pos_t {
	PI p;
	int cnt;
	bool operator()( const pos_t& a, const pos_t& b ) const {
		return a.p < b.p;
	}
};

const LL MOD = 1000002013;
priority_queue<PI> pq;

LL dist_cost( int from, int to, LL N ) {
	if( from == to ) return 0;
	LL n = to-from;
	LL tmp = (n*(n-1)/2)%MOD;
	LL res = (n*N -tmp + MOD)%MOD;
	return res;
}

int main() {
	int cases;
	cin >> cases;
	for( int caseid = 1; caseid <= cases; ++caseid ) {
		cout << "Case #" << caseid << ": ";
		int N;
		int M;
		vector<trip_t> trips;
		cin >> N >> M;
		trips.resize(M);
		LL regular_cost = 0;
		for( int i = 0; i < M; ++i ) {
			cin >> trips[i].from >> trips[i].to >> trips[i].cnt;
			regular_cost = (regular_cost + dist_cost( trips[i].from, trips[i].to, N) * trips[i].cnt )%MOD;
		}
		vector<pos_t> pos;
		for( int i = 0; i < M; ++i ) {
			pos_t x;
			x.p = PI(trips[i].from,0);
			x.cnt = trips[i].cnt;
			pos.push_back(x);
			x.p = PI(trips[i].to,1);
			x.cnt = trips[i].cnt;
			pos.push_back(x);
		}
		sort( pos.begin(), pos.end(), pos_t() );
		while( !pq.empty() ) pq.pop();
		LL cost = 0;
		for( int i = 0; i < (int)pos.size(); ++i ) {	
			if( pos[i].p.second == 0 ) {
				// enter
				pq.push( PI(pos[i].p.first,pos[i].cnt) );
			} else {
				// leave
				int cnt = pos[i].cnt;
				while( cnt > 0 ) {
					assert( !pq.empty() );
					PI p = pq.top(); pq.pop();
					cost = (cost + dist_cost( p.first, pos[i].p.first, N ) * min( cnt, p.second ) )%MOD;
					if( p.second > cnt ) {
						pq.push( PI(p.first,p.second-cnt));
						cnt = 0;
					} else if( p.second == cnt ) {
						cnt = 0;
					} else {
						cnt -= p.second;
					}
				}
			}
		}
		assert( pq.empty() );
		cost %= MOD;
		LL tmp = (regular_cost - cost + MOD)%MOD;
		cout << tmp << endl;
	}
	return 0;
}

