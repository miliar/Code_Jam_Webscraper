#include <iostream>
#include <string>
using namespace std;
int main () {
	int T; cin >> T;
	for (int C=1;T--;C++) {
		int n; cin >> n;
		string s; cin >> s;
		int aud = 0; int ans = 0;
		for (int i=0;i<n+1;i++) {
			int v = s[i]-'0';
			if (i > aud) {
				ans += i-aud;
				aud += i-aud;
			}
			aud += v;
		}
		cout << "Case #" << C << ": " << ans << endl;

	}
	return 0;
}