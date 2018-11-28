#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;
int main () {
	freopen ("C:\\Users\\shreshtha24\\Desktop\\input.txt", "r", stdin);
	freopen ("C:\\Users\\shreshtha24\\Desktop\\ans1.txt", "w", stdout);
	int itr, jj, k = 1, t, nnn, c, r;
	cin >> t;
	while ( t--) {
		vector <double> ab;
		vector <double> ab2;
		double tr;
		cin >> nnn;
		for ( itr = 0; itr < nnn; itr ++) {
			cin >> tr;
			ab.push_back(tr);
		}
		for ( jj = 0; jj < nnn; jj ++) {
			cin >> tr;
			ab2.push_back(tr);
		}
	
		sort (ab.begin(), ab.end());
		sort (ab2.begin(), ab2.end());
		jj = 0;
		c = 0;
		r = 0;
		for ( itr = 0; itr < nnn; itr ++) {
			if ( jj < nnn && ab[itr] > ab2[jj] ) {
				c ++;
				jj ++;
			}
		}
		jj = nnn-1;
		for ( itr = nnn-1; itr >= 0; itr --) {
			for ( ; jj >= 0; jj --) {
				if ( ab2[itr] > ab[jj] ) {
					r ++;
					jj --;
					break;
				}
			}
		}
		cout << "Case #" << k << ": " << c << " " << (nnn-r) << endl;
		k ++;
	}
	return 0;
}
