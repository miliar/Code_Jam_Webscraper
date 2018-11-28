#include <iostream>
#include <string>
using namespace std;

int main () {
	string s;
	int t;
	int smax;
	cin >> t;
	for (int j=0;j<t;j++) {
		cin >> smax >> s;
		int ans = 0;
		int count = 0;
		for (int i=0;i<=smax;i++) {
			if ((int)s[i]-48 > 0) {
				if (count + ans < i) ans = ans + (i-(count+ans));
			}
			count = count + (int)s[i]-48;
		}
		cout << "Case #" << j+1 << ": " << ans << endl;
	}
}