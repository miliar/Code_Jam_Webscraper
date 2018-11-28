#include<iostream>
#include<string>
using namespace std;
int main() {
	int t, s, m, ans;
	string str;
	cin >> t;
	for(int j = 0; j < t; j++){
		cin >> s;
		cin.get();
		cin >> str;
		m = 0;
		ans = 0;
		for(int i = 0; i <= s; i++) {
			if(m < i) {
				ans += (i-m);
				m = i;
			}
			m += (str[i] - '0');
		}
		cout << "Case #" << j+1 << ": " << ans << "\n";
	}
	return 0;
}
