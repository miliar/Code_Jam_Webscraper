#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

#define ZERO(v) memset( (v), 0, sizeof((v)))

const size_t MAXN = 100;
const size_t MAXL = 100;

char strings[MAXN][MAXL+1];
char reduced[MAXN][MAXL+1];
size_t cts[MAXN][MAXL];

size_t best_cost( size_t i, size_t N ) {
	size_t best_so_far = MAXL;
	for( size_t attempt = 1; attempt <= MAXL; ++attempt ) {
		size_t this_cost = 0;
		for( size_t k = 0; k < N; ++k ) {
			if( cts[k][i] < attempt ) this_cost += attempt - cts[k][i];
			else this_cost += cts[k][i] - attempt;
		}
		best_so_far = min(best_so_far, this_cost);
	}
	return best_so_far;
}

int main() {
	size_t T; cin >> T;
	for( size_t Case = 1; Case <= T; ++Case ) {
		cout << "Case #" << Case << ": ";
		ZERO(strings); ZERO(reduced); ZERO(cts);
		size_t N; cin >> N;
		for( size_t i = 0; i < N; ++i ) {
			cin >> strings[i];
		}
		for( size_t k = 0; k < N; ++k ) {
			reduced[k][0] = strings[k][0];
			size_t j = 1;
			size_t L = strlen(strings[k]);
			cts[k][0] = 1;
			for( size_t i = 1; i < L; ++i ) {
				if( strings[k][i] == reduced[k][j-1] ) {
					++cts[k][j-1];
				}
				else {
					reduced[k][j++] = strings[k][i];
					cts[k][j-1] = 1;
				}
			}
			reduced[k][j] = '\0';
		}
		bool feasible = true;
		for( size_t k = 1; feasible && k < N; ++k ) {
			if( strcmp( reduced[k-1], reduced[k] ) != 0 ) {
				feasible = false;
			}
		}
		if( !feasible ) {
			cout << "Fegla Won" << endl;
			continue;
		}
		size_t ttl_cost = 0;
		for( size_t i = 0; i < strlen(reduced[0]); ++i ) {
			ttl_cost += best_cost( i, N );
		}
		cout << ttl_cost << endl;
	}
	return 0;
}
