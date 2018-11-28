#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;

typedef long long LL ;

int T;
int nCase = 1;

int N, M;

int pos[2000];
struct Pass
{
	int begin, end, num;
	Pass(int b, int e, int n) 
		: begin(b), end(e), num(n) {}
};
vector<Pass> pass;

void input()
{
	pass.clear();
	cin >> N >> M ;
	for ( int i=0;i<M;++i ) {
		int b, e, n;
		cin >> b >> e >> n;
		pass.push_back( Pass(b, e, n) );
	}
}

LL cnt[2001] ;

LL cost ( int diff ) 
{
	if ( diff < 0 ) diff = 0-diff;
	return (2*N-diff+1)*diff/2LL ;
}

LL solv()
{
	LL expected = 0 ;
	for ( int i=0;i<M;++i ) {
		pos[i<<1] = pass[i].begin;
		pos[2*i+1] = pass[i].end;
		expected += cost(pass[i].end-pass[i].begin)*pass[i].num;
	}
	sort(pos, pos+2*M);
	int npos = 1;

	map<int, int> index ;
	index[pos[0]] = 0;
	for ( int i=1;i<2*M;++i ) {
		if ( pos[i] != pos[i-1] ) {
			index[pos[i]] = npos;
			pos[npos++] = pos[i] ;
		}
	}
	
	memset(cnt, 0, sizeof (cnt));
	for ( int i=0;i<M;++i ) {
		int begin = index[pass[i].begin];
		int end = index[pass[i].end];
		// cout << begin << ", " << end << ":" << pass[i].num << endl;
		if ( begin < end ) {
			for ( int j=begin;j<end;++j )
				cnt[j] += pass[i].num ;
		} else{
			for ( int j=end;j<begin;++j )
				cnt[j] -= pass[i].num ;
		}
	}
	
	LL ans = 0;
	
	for ( int i=0;i<npos; ) {
		if ( cnt[i] != 0 ) {
			int begin = pos[i];
			LL mx = cnt[i];
			int j = i+1;
			while ( cnt[j] != 0 ) {
				mx = min(mx, cnt[j]);
				++j ;
			}
			// cout << begin << ", " << pos[j] << ": " << mx << "*" << cost(pos[j]-pos[i])<< endl;
			ans += cost(pos[j]-pos[i])*mx;
			for ( int k=i;k<j;++k ) {
				cnt[k] -= mx;
			}
		} else {
		 ++ i;
		}
	}
	// cout << expected << ' ' << ans << endl;
	return expected - ans ;
}

int main()
{
	cin >> T;
	while ( T -- > 0 ) {
		input();
		cout << "Case #" << nCase++ << ": " << solv() << endl;
	}
	return 0;
}
