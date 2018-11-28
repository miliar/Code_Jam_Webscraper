#include <bits/stdc++.h>

using namespace std;

int getint(char a) {
	return (a - 48);
}

int main() {
	int sum,i,k,tc, val, sol;
	cin >> tc;
	for (i = 1; i <= tc; i++) {
		sum = 0;
		int sh;
		string a;
		cin >> sh;
		cin >> a;
		val = getint(a[0]);
	//	cout << val << endl;
		sum = val;
		sol = 0;
		for (k = 1; k < a.length(); k++) {
				if (k <= sh) {
					val = getint(a[k]);
				//	cout << val << endl;
					if (val == 0) {
						continue;
					}
					if (k > sum) {
						sol += k - sum;
						sum += sol + val;
					}
					else {
						sum += val;
					}
					
					

				}
	//		cout << sol <<" " << k << " " << sum << endl;
		}
		cout << "Case #" << i <<": " << sol << endl;
	}
	return 0;
}