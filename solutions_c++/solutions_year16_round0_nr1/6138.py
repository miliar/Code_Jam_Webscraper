#include <bits/stdc++.h>
using namespace std;

string int2str(int a) {
	ostringstream oss;
	oss << a;
	return oss.str();
}

int main() {
	int tc, n;

	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> tc;

	for(int i=1; i<=tc; i++) {
		bool sl[10];
		for(int j=0; j<10; j++) sl[j] = false;
		int cnt = 0;
		int ans = 0;
		cin >> n;

		int tmpN = n;
		if(n == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else {
			int index = 2;
			while(true) {
				string tmp = int2str(n);
				for(int j=0; j<tmp.length(); j++) {
					if(sl[tmp[j] - '0'] == false) {
						cnt++;
						sl[tmp[j] - '0'] = true;
					}
				}

				if(cnt >= 10) {
					ans = n;
					break;
				}
				else {
					n = index * tmpN;
					index++;
				}				
			}

			cout << "Case #" << i << ": " << ans << endl;
		}
	}

	return 0;
}

