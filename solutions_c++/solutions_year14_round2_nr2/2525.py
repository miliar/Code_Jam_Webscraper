#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);

	int T;
	cin >> T;
	for (int t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";

		long a, b, k, r = 0;
		cin >> a >> b >> k;

		for (long i=0; i<a; i++){
			for (long j=0;j<b;j++) {
				if ((i&j) < k)
					r++;
			}
		}

		cout << r << endl;
	}

	return 0;
}
