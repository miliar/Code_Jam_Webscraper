#include <iostream>
#include <cstdio>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

int t;
int n, P[1002];

int main(){

	freopen( "B-large.in" , "r", stdin  );
	freopen( "B-large.out", "w", stdout );
	optimizar_io 

	cin >> t;
	for( int c = 1; c <= t; c++ ){
	
		cin >> n;
		for( int i = 1; i <= n; i++ )
			cin >> P[i];
			
		int ans = 1000;
		for( int k = 1; k <= 1000; k++ ){
			int tmp = 0;
			for( int j = 1; j <= n; j++ )
				tmp += ( P[j] - 1 ) / k;
			ans = min( ans, tmp + k );
		}
		cout << "Case #" << c << ": " << ans << "\n";
	
	}
	return 0;

}
