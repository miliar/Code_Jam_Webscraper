#include <iostream>
#include <cstdio>

using namespace std;

int t;
int n, m;
int arr[150][150];

bool solve() {
	for ( int i = 0 ; i < n ; ++i ) {
		for ( int j = 0 ; j < m ; ++j ) {

			bool flag1 = true;

			for ( int k = 0 ; k < m ; ++k )
				if ( arr[i][k] > arr[i][j] )
					flag1 = false;

			bool flag2 = true;
			for ( int k = 0 ; k < n ; ++k )
				if ( arr[k][j] > arr[i][j] )
					flag2 = false;

			if ( !flag1 && !flag2 ) return false;
		}
	}
	return true;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	
	scanf("%d", &t);
	for ( int i = 0 ; i < t ; ++i ) {
		scanf("%d%d", &n, &m);

		for ( int a = 0 ; a < n ; ++a )
			for ( int b = 0 ; b < m ; ++b )
				scanf("%d", &arr[a][b]);

		printf("Case #%d: ", i + 1);
		puts( (solve() ? "YES" : "NO") );
	}
	
	return 0;
}