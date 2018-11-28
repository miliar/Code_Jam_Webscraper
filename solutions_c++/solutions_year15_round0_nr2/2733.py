#include <bits/stdc++.h>
using namespace std;

int p[1005];

int main () {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int d;
		cin >> d;
		for(int i = 0; i < d; i++)
			cin >> p[i];
		int res = 2000;
		for(int i = 1; i <= 1000; i++) {
			int tmp = i;
			for(int j = 0; j < d; j++) {
				if(p[j] > i) {
					tmp += p[j]/i - 1;
					if(p[j]%i != 0)
						tmp++;
				}
			}
			res = min(res, tmp);
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}
