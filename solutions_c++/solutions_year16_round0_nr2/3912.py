#include <bits/stdc++.h>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int t, sol;
	string s;
	cin >> t;
	
	for (int i = 1; i <= t; ++i) {
		sol = 0;
		cin >> s;
		int len = s.length();
		char c = '-';
		
		// bounded by 2 * len
		int j = len - 1;
		while (1) {
			if (c == '+')
				c = '-';
			else c = '+';
			
			while (j >= 0 && s[j] == c)
				--j;
		
			if (j == -1) {
				cout << "Case #" << i << ": "<< sol <<  "\n";
				break;
			}
			
			++sol;
		}
	}
	
	return 0;
}
