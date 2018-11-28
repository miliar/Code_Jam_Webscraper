#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	for (int tc = 0; tc < n; tc++) {
		int m;
		cin >> m;
		if (m == 0) {
			cout << "Case #" << tc+1 << ": INSOMNIA" << endl;
			continue;
		}
		
		vector<bool> seen(256, false);
		int c = 1;
		bool tf = true;
		while (tf) {
			tf = false;
			int k = c * m;
			c ++;
			stringstream ss;
			ss << k;
			string str = ss.str();
			for (int i = 0; i < str.size(); i ++) {
				seen[str[i]] = true;
			}
			for (int i = (int)'0'; i <= (int)'9'; i++){
				if (!seen[i]) {
					tf = true;
					break;
				}
			}
		}
		cout << "Case #" << tc+1 << ": " << (c-1)*m << endl;
	}
	// your code goes here
	return 0;
}