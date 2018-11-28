#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <cmath>

using namespace std;

const int MAXN = 128;

int n;
char s[MAXN][MAXN];

void read() {
	int i;

	scanf ( "%d", &n );

	for ( i = 0; i < n; ++ i ) {
		scanf ( "%s", s[i] );
	}
}

int mod ( int x ) {
	if ( x < 0 )  return -x;
	return x;

}

void solve ( int test ) {
	int i, j, k;

	vector < pair < char, int > > v[MAXN];
	vector < int > av;

	for ( i = 0; i < n; ++ i ) {
		int sz = ( int ) strlen ( s[i] );

		for ( j = 0; j < sz; ++ j ) {
			char c = s[i][j];
			int cnt = 0;
			while ( s[i][j] == c ) {
				cnt ++;
				j ++;
			}
			j --;
			v[i].push_back ( make_pair ( c, cnt ) );
		}
	}

	int ret = 0;
	int sz = ( int ) v[0].size();

	for ( i = 1; i < n; ++ i ) {
		if ( sz != ( int ) v[i].size() ) {
			printf ( "Case #%d: Fegla Won\n", test );
			return;
		}
	}

	for ( i = 0; i < sz; ++ i ) {
		double sum = 0;
		char c = v[0][i].first;
		for ( j = 0; j < n; ++ j ) {
			if ( v[j][i].first != c ) {
				printf ( "Case #%d: Fegla Won\n", test );
				return;
			}
			sum += (double) v[j][i].second;
		}

		av.push_back ( ( int ) sum / n );
	}

	for ( i = 0; i < sz; ++ i ) {
		for ( j = 0; j < n; ++ j ) {
			ret += mod ( av[i] - v[j][i].second );
		}
	}

	printf ( "Case #%d: %d\n", test, ret );

}

int main() {
	int i, tests;

	scanf ( "%d", &tests );

	for ( i = 0; i < tests; ++ i ) {
		read();
		solve ( i + 1 );
	}

	return 0;

}