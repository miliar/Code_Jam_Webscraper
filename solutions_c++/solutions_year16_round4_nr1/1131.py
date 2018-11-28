#include<bits/stdc++.h>

using namespace std;

string ch[3] = { "R" , "P" , "S" };
int a[15][1<<15] , n;

string build( int dep , int i ) {
	if( dep == n )
		return ch[i];
	string x = build( dep+1 , i ) , y = build( dep+1 , (i+2)%3 );
	if( x < y )
		return x+y;
	return y+x;
}

void init() {
	memset( a , 0 , sizeof a );
	a[0][0] = 1;
	for( int i = 1 ; i <= 12 ; i++ )
		for( int j = 0 ; j < 3 ; j++ )
			a[i][j] = a[i-1][j]+a[i-1][(j+1)%3];
}

int main() {
	init();
	int t , c[5];
	cin >> t;
	for( int ca = 1 ; ca <= t ; ca++ ) {
		cin >> n;
		for( int i = 0 ; i < 3 ; i++ )
			scanf( "%d" , &c[i] );
		cout << "Case #" << ca << ": ";
		bool flag = 0;
		for( int i = 0 ; i < 3 ; i++ ) {
			bool b = 1;
			for( int j = 0 ; j < 3 ; j++ )
				b &= c[(i+j)%3] == a[n][j];
			if( b ) {
				flag = 1;
				cout << build( 0 , i ) << endl;
				break;
			}
		}
		if( !flag )
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
