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
	int itr1, itr2, k = 1, t, ns, count, r;
	vector <double> ab;
	vector <double> ab2;
	cin >> t;
	while ( t--) {
		ab.clear();
		ab2.clear();
		double tr;
		cin >> ns;
		for ( itr1 = 0; itr1 < ns; itr1 ++) {
			scanf("%lf", &tr);
			ab.push_back(tr);
		}
		for ( itr2 = 0; itr2 < ns; itr2 ++) {
			scanf("%lf", &tr);
			ab2.push_back(tr);
		}
	
		sort (ab.begin(), ab.end());
		sort (ab2.begin(), ab2.end());
		itr2 = 0;
		count = 0;
		r = 0;
		for ( itr1 = 0; itr1 < ns; itr1 ++) {
			if ( itr2 < ns && ab[itr1] > ab2[itr2] ) {
				count ++;
				itr2 ++;
			}
		}
		itr2 = 0;
		itr2 = ns-1;
		for ( itr1 = ns-1; itr1 >= 0; itr1 --) {
			for ( ; itr2 >= 0; itr2 --) {
				if ( ab2[itr1] > ab[itr2] ) {
					r ++;
					itr2 --;
					break;
				}
			}
		}
		cout << "Case #" << k << ": " << count << " " << (ns-r) << endl;
		k ++;
	}
	return 0;
}
