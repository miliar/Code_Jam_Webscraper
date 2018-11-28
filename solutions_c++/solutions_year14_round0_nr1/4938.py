#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
using namespace std;
int main () {
	freopen ("C:\\Users\\shreshtha24\\Desktop\\ans.txt", "w", stdout);
	int t, n, m, i, j, k = 1;
	cin >> t;
	while ( t --) {
		int c = 0, r;
		int a[4][4];
		int b[4][4];
		cin >> n ;
		for ( i = 0; i < 4; i ++) {
			for ( j = 0; j < 4; j ++) {
				cin >> a[i][j];
			}
		}
		cin >> m;
		for ( i = 0; i < 4; i ++) {
			for ( j = 0; j < 4; j ++) {
				cin >> b[i][j];
			}
		}
		n --;
		m --;
		c = 0;
		for ( i = 0; i < 4; i ++) {
			for ( j = 0; j < 4; j ++) {
				if ( a[n][i] == b[m][j] ) {
					c ++;
					r = a[n][i];
				}
			}
		}
		if ( c == 1 )
			cout << "Case #" << k << ": " << r << endl;
		else if ( c > 1 )
			cout << "Case #" << k << ": Bad magician!" << endl;
		else if ( c == 0) 
			cout << "Case #" << k << ": Volunteer cheated!" << endl;
		k ++;
	}
	return 0;
}