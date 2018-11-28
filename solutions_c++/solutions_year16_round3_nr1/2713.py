#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <iterator>
#include <functional>
#include <list>
using namespace std;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int n;

	cin >> n;



	for ( int i  = 0; i < n; i++) {



		string result = "";
		int c; cin >> c;

		int p[c];

		int im, iml;
		int m = 0, ml = 0;

		string ch;

		for ( int j = 0; j < c; j++) {
			ch += ('A' + j);
			cin >> p[j];
			//cout << p[j];
			if ( m <= p[j]) {
				m = p[j]; im = j;
			}
		}


		for ( int j = 0 ; j < c ; j++ ) {
			if ( j == im ) continue;

			if ( ml <= p[j]) {
				ml = p[j]; iml = j;
			}
		}

	//	if ( i != 44 ) continue;

		//cout << im << " " << iml << endl;


		while ( m > ml) {
			int diff = m - ml;
			if ( diff > 2 )  diff = 2;

			result += ch[im];

			if ( diff > 1) {

				result += ch[im];
			}

			result += " ";

			m -= diff;
			p[im] -= diff;
		}



		bool one = false;

		for ( int j = 0; j < c ;j++) {
			//cout << "(" << j << ")"<< p[j] << endl;
			if ( j == im || j == iml) continue;

			for ( int k = 0; k < p[j]; k++) {
				result += ch[j];
				one  = !one;

				if (!one) {
					result += " ";
				}

			//	cout << result << endl;
			}
		}


		if (one) result += " ";

		for ( int j = 0; j < m; j++) {
			result +=ch[im];
			result +=ch[iml];
			result +=" ";
		}






		cout << "Case #" << ( i + 1) << ": " << result << endl;
	}


	return 0;

}
