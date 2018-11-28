#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;
int main () {
	freopen ("C:\\Users\\shreshtha24\\Desktop\\ans.txt", "w", stdout);
	int i, j, k = 1, t, n, c, r;
	cin >> t;
	while ( t--) {
		double a[1005], b[1005];
		cin >> n;
		for ( i = 0; i < n; i ++) {
			cin >> a[i];
		}
		for ( j = 0; j < n; j ++) {
			cin >> b[j];
		}
		sort (a, a+n);
		sort (b, b+n);
		j = 0;
		c = 0;
		r = 0;
		for ( i = 0; i < n; i ++) {
			if ( j < n && a[i] > b[j] ) {
				c ++;
				j ++;
			}
		}
		j = n-1;
		for ( i = n-1; i >= 0; i --) {
			for ( ; j >= 0; j --) {
				if ( b[i] > a[j] ) {
					r ++;
					j --;
					break;
				}
			}
		}
		cout << "Case #" << k << ": " << c << " " << (n-r) << endl;
		k ++;
	}
	return 0;
}
