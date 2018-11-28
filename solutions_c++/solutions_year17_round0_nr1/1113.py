#include<bits/stdc++.h>
using namespace std;

int main() {
	 int t; cin >> t;
	 
	 for(int c=1; c<=t; c++) {
		string s; cin >> s;
		int k; cin >> k;
		int n = s.length();
		
		int count = 0;
		for(int i=0; i<=n-k; i++) {
			if( s[i]=='-' ) {
				count++;
				for(int j=0; j<k; j++) {
					if( s[i + j] == '+' ) {
						s[i+j] = '-';
					} else {
						s[i+j] = '+';
					}
				}
			}
		}
		
		bool possible = true;
		for(int i=n-k+1; i<n; i++) {
			if( s[i] == '-' ) {
				possible = false;
				break;
			}
		}
		
		cout << "Case #" << c << ": ";
		if(possible) {
			cout << count << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	 }
}