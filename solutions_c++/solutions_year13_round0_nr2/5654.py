#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;
	
void main1( int t1 )
{
	int i, j, k, n, m, max, min;
	string s1, s2;
	s1 = "NO";
	s2 = "YES";
	cin >> n >> m;
	int a[n][m], b[n][m];
	max = 1;
	min = 100;
	
	for ( i = 0; i < n; i ++ ) {
		
		for ( j = 0; j < m; j ++ ) {
			cin >> k;
			a[i][j] = k;
			if ( k > max ) {
				max = k;
			}
			if ( k < min ) {
				min = k;
			}
		}
		
	}
	
	for ( i = 0; i < n; i ++ ) {
		
		for ( j = 0; j < m; j ++ ) {
			b[i][j] = max;
		}
		
	}
	
	
	
	if ( min != max ) {
	
		for ( i = 0; i < n; i ++ ) {	
			if ( a[i][0] != max ) {
				j = 1;
				
				while ( j < m ) {
					if ( a[i][j] > a[i][0] ) {
						break;
					}
					j ++;
				}
				
				if ( j == m ) {
					j = 0;
					
					while ( j < m ) {
						b[i][j] = a[i][0];
						j ++;
					}
				}
			}
		}
		
		for ( j = 0; j < m; j ++ ) {
			if ( a[0][j] != max ) {
				i = 1;
				
				while ( i < n ) {	
					if ( a[i][j] > a[0][j] ) {
						break;
					}
					i ++;
				}
				
				if ( i == n ) {
					i = 0;
					
					while ( i < n ) {
						b[i][j] = a[0][j];
						i ++;
					}
				}
			}
		}
		
		for ( i = 0; i < n; i ++ ) {
		
			for ( j = 0; j < m; j ++ ) {
				if ( a[i][j] != b[i][j] ) {
					cout << "Case #" << t1 << ": " << s1 << "\n";
					return;
				}
			}
		}
		
	}

	cout << "Case #" << t1 << ": " << s2 << "\n";
}

int main()
{
	int i, t;
	cin >> t;
	
	for ( i = 1; i <= t; i ++ ) {
		main1( i );
	}
	
	return 0;
}