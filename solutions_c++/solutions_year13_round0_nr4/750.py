#include <map>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;

int k , n;
map < int , int > a;
vector < int > c[512];
int key[512];
int used[1 << 20];
int next[1 << 20];

void read() {
	int i , x , j;
	
	a.clear();
	scanf ( "%d%d" , &k , &n );
	for (i = 1; i <= k; i++) {
		scanf ( "%d" , &x );
		a[x] ++;
	}
	
	for (i = 0; i < n; i++) {
		scanf ( "%d" , &key[i] );
		c[i].clear();
		scanf ( "%d" , &j );
		while ( j -- ) {
			scanf ( "%d" , &x );
			c[i].push_back ( x );
		}
	}
}

int go ( int mask , map < int , int > a ) {
	if ( mask == (1 << n) - 1 ) return 1;
	if ( used[mask] ) return 0;
	used[mask] = 1;
	int i , j;
	map < int , int > b;
	
	for (i = 0; i < n; i++) {
		if ( !(mask & (1 << i)) && a[ key[i] ] > 0 ) {
			b = a;
			b[ key[i] ] --;
			for (j = 0; j < (int)c[i].size(); j++) {
				b[ c[i][j] ] ++;
			}
			
			if ( go ( mask | (1 << i) , b ) ) {
				next[mask] = i;
				return 1;
			}
		}
	}
	
	return 0;
}

void solve() {
	memset ( used , 0 , sizeof used );
	if ( go ( 0 , a ) ) {
		int mask = 0 , pr = 0;
		
		while ( mask != (1 << n) - 1 ) {
			if ( pr ) printf ( " " );
			printf ( "%d" , next[mask] + 1 );
			pr = 1;
			mask |= 1 << next[mask];
		}
		printf ( "\n" );
	} else {
		printf ( "IMPOSSIBLE\n" );
	}
}

int main() {
	int i , cases;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases;i++) {
		read();
		printf ( "Case #%d: " , i );
		solve();
	}
	
	return 0;
}
