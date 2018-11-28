#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	int tc = 0;

	while(T--) {
		tc++;
		int max;
		string str;
		cin >> max;
		cin >> str;

		int count = 0;
		int ans = 0;
		for(int i=0; i<(int)str.size(); i++) {
			if(count>=i) {
				count += (int)(str[i] - '0');
			}
			else {
				while(count < i) {
					count++;
					ans++;
				}
				count += (int)(str[i] - '0');
			}
		}

		cout << "Case #" << tc << ": " << ans << endl;
	}
}