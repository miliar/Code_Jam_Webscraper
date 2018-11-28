#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <iomanip>

using namespace std;

int main() {
	int numCases;
	cin >> numCases;

	for(int c = 0; c < numCases; c++) {
		int s, n;
		cin >> s >> n;

		vector<int> a(n);
		for(int i = 0; i < n; i++) {
			cin >> a[i];
		}

		sort(a.begin(), a.end());

		int m = 0;
		int pm = 0;
		for(int i = 0; i < a.size(); i++) {
			if ( s > a[i] ) {
				//cout << "s = " << s << ", absorbed " << a[i] << endl;
				s += a[i];				
				continue;
			}

			int r = a.size() - i;
			int p = s - 1;
			if ( p == 0 ) {
				m += r;
				break;
			}

			int s2 = s;
			int am = 0;
			while(s2 <= a[i]) {
				s2 += (s2 - 1);
				am++;
			}
			// cout << "s = " << s << endl;
			// cout << "am = " << am << endl;
			if ( am >= r ) {
				m += r;
				break;
			}

			pm = m + r;

			m += am;
			if ( m >= pm ) {
				m = pm;
				break;
			}

			s = s2 + a[i];
		}

		printf("Case #%d: ", c+1);
		cout << m << endl;
	}

	return 1;
}