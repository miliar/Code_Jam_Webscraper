#include <bits/stdc++.h>
using namespace std;
int main() {
	int t;
	int run = 1;
	cin >> t;
	for(run = 1; run <= t; run++) {
		int input[105] = {0};
		int k = 0;
		string str;
		cin >> str;
		int flag = 0;
		int i;
		char ch = str[0];
		if(ch == '+') {
			input[k++] = 1;
		} else {
			input[k++] = 0;
		}
		for(i = 0; i < str.size(); i++) {
			if(str[i] == ch) {
				continue;
			} else {
				ch = str[i];
				if(ch == '+') {
					input[k++] = 1;
				} else {
					input[k++] = 0;
				}
			}
		}
		int ans = 0;
		for(i = 0; i < k; i++) {
			if(i == 0 && input[i] == 0) {
				ans += 1;
			} else if(input[i] == 0) {
				ans += 2;
			}
		}
		cout << "Case #" << run << ": " << ans << endl;
	}
	return 0;
}