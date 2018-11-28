#include <bits/stdc++.h>

using namespace std;

int main(){
	
	freopen("in", "r", stdin );
	freopen("out", "w", stdout );
	
	int t;
	
	cin >> t;
	
	for( int w = 1; w <= t; ++w ){
		int k, c, s;
		cin >> k >> c >> s;
		
		int need = 0;
		int positions[s + 1];
		
		if( c == 1 ){
			need = k;
			for( int i = 0; i < need; ++i ){
				positions[i] = i + 1;
			}
		}
		else{
			
			for( int i = 1; i <= k; i += 2 ){
				int indx = ( i - 1 ) * k + i;
				if( i != k ){
					++indx;
				}
				
				positions[need++] = indx;
				
				if( need > s ){
					break;
				}
			}
		}
		cout << "Case #" << w <<": ";
		
		if( need > s ){
			cout << "IMPOSSIBLE" << endl;
		}
		else{
			for( int i = 0; i < need - 1; ++i ){
				cout << positions[i] << " ";
			}
			cout << positions[need - 1] << endl;
		}
		
	
	}

	return 0;
}
