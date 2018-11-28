#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

#define FOR(v,l,u) for( size_t v = l; v < u; ++v )
#define ZERO(v) memset((v), 0, sizeof((v)));

const size_t MAXN = 10000;

size_t C;
size_t N;
size_t X[MAXN];

size_t find_paired() {
	size_t lb = 0, ub = N/2+1;
	while( ub - lb > 1 ) {
		size_t mb = (lb+ub)/2;
		bool ok = true;
		FOR(i,0,mb) {
			if( X[i] + X[2*mb-1-i] > C ) ok = false;
		}
		if( ok ) lb = mb;
		else ub = mb;
	}
	return lb;
}

int main() {
	size_t T; cin >> T;
	FOR(Case,1,T+1) {
		ZERO(X);
		cin >> N >> C;
		FOR(i,0,N) cin >> X[i];
		sort(X, X+N);
		size_t n_paired = find_paired();
		cout << "Case #" << Case << ": ";
		cout << N - n_paired << endl;
	}
	return 0;
}
