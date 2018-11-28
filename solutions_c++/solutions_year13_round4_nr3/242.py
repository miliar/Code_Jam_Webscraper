#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;

int n;
int a[32];
int b[32];
vector < int > dp[1 << 20];
int u[1 << 20];

void read() {
	int i;
	
	scanf ( "%d" , &n );
	for (i = 0; i < n; i++) {
		scanf ( "%d" , &a[i] );
	}
	for (i = 0; i < n; i++) {
		scanf ( "%d" , &b[i] );
	}
}

vector < int > go ( int mask , int put = 1 ) {
	vector < int > &ans = dp[mask];
	if ( u[mask] ) return ans;
	u[mask] = 1;
	
	int i , j;
	int left , right;
	int ss = 0;
	vector < int > cur;
	
	for (i = 0; i < n; i++) {
		if ( mask & (1 << i) ) continue;
		
		left = right = 1;
		
		for (j = 0; j < i; j++) {
			if ( mask & (1 << j) ) {
				left = max ( left , a[j] + 1 );
			}
		}
		
		for (j = n - 1; j > i; j--) {
			if ( mask & (1 << j) ) {
				right = max ( right , b[j] + 1 );
			}
		}
				
		if ( left != a[i] || right != b[i] ) continue;
		
	//	if ( put == 10 ) printf ( "%d %d   %d    %d\n" , left , right , i , mask );

		
		cur = go ( mask | (1 << i) , put + 1 );
		int cnt = 0;
		for (j = 0; j < n; j++) cnt += (cur[j] != 0);
		
		if ( cnt != n - put ) continue;
		
		cur[i] = put;
		
		if ( cur < ans || !ss ) {
			ans = cur;
			ss = 1;
		}
	}
	
//	printf ( "%d   " , put );
//	for (i = 0; i < n; i++) printf ( "%d " , ans[i] ); printf ( "\n" );
	
	return ans;
}

void solve() {
	int i , j;
	
	memset ( u , 0 , sizeof u );
	for (i = 0; i < (1 << n); i++) {
		dp[i].clear();
		for (j = 0; j < n; j++) dp[i].push_back ( 0 );
	}
	
	vector < int > ans = go ( 0 );
	for (i = 0; i < n; i++) {
		printf ( "%d" , ans[i] );
		
		if ( i == n - 1 ) printf ( "\n" );
		else printf ( " " );
	}
}

int main() {
	int i , cases;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		read();
		printf ( "Case #%d: " , i );
		solve();
	}
	
	return 0;
}
